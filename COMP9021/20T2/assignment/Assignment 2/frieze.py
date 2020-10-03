# Insert your code here
import os.path
import copy


class Frieze:
    def __init__(self, filename=None):
        self.vertical, self.filename = 0, filename
        if filename is not None and os.path.exists(filename):
            with open(filename) as open_file:
                self.lines, self.period = [], 0
                for line in open_file:
                    if not line.strip():
                        continue
                    line, length = line.split(), []
                    for i in line:
                        if not i.isdigit():
                            raise FriezeError('Incorrect input.')
                        j = int(i)
                        if not (0 <= j <= 15):
                            raise FriezeError('Incorrect input.')
                        length.append(j)
                    if not (5 <= len(length) <= 51):
                        raise FriezeError('Incorrect input.')
                    self.lines.append(length)
            self.height, self.leng = len(self.lines), len(self.lines[0])
            if not (3 <= self.height <= 17):
                raise FriezeError('Incorrect input.')
            i, j, k, m, n, p = 0, 0, 0, 0, 0, 0
            while i <= self.height - 1:
                if len(self.lines[i]) != self.leng:
                    raise FriezeError('Incorrect input.')
                i += 1
            while j <= self.height - 1:
                binary_right = '0' * (6 - len(bin(self.lines[j][-1]))) + bin(self.lines[j][-1])[2:]
                if binary_right[:3] != '000':  # rightmost line should only be |
                    raise FriezeError('Input does not represent a frieze.')
                j += 1
            while m <= len(self.lines[-1]) - 1:
                binary_down = '0' * (6 - len(bin(self.lines[-1][m]))) + bin(self.lines[-1][m])[2:]
                if binary_down[0] != '0':  # last line should not be \
                    raise FriezeError('Input does not represent a frieze.')
                m += 1
            while n <= self.height - 2:  # no crossing segments like X
                j = 0
                while j <= self.leng - 2:
                    binary_1 = '0' * (6 - len(bin(self.lines[n][j]))) + bin(self.lines[n][j])[2:]
                    binary_2 = '0' * (6 - len(bin(self.lines[n + 1][j]))) + bin(self.lines[n + 1][j])[2:]
                    if binary_1[0] == '1' and binary_2[2] == '1':
                        raise FriezeError('Input does not represent a frieze.')
                    j += 1
                n += 1
            while k <= self.leng - 1:
                binary_up = '0' * (6 - len(bin(self.lines[0][k]))) + bin(self.lines[0][k])[2:]
                if binary_up[2:] != '00':  # first line should be - or \
                    raise FriezeError('Input does not represent a frieze.')
                k += 1
            # a pattern at least equal to 2 that is fully repeated at least twice in the horizontal dimension
            while p <= self.leng - 2:  # top and bottom line
                binary_3 = '0' * (6 - len(bin(self.lines[0][p]))) + bin(self.lines[0][p])[2:]
                binary_4 = '0' * (6 - len(bin(self.lines[-1][p]))) + bin(self.lines[-1][p])[2:]
                if int(binary_3[1]) == 0:
                    raise FriezeError('Input does not represent a frieze.')
                if int(binary_4[1]) == 0:
                    raise FriezeError('Input does not represent a frieze.')
                p += 1
            q = 1
            while q <= (self.leng - 1) // 2:
                if self.period:  # smallest period
                    break
                binary_5 = '0' * (6 - len(bin(self.lines[0][q]))) + bin(self.lines[0][q])[2:]
                binary_6 = '0' * (6 - len(bin(self.lines[0][2 * q]))) + bin(self.lines[0][2 * q])[2:]
                if self.lines[0][0: q] == self.lines[0][q: 2 * q] and binary_5[3] == binary_6[3] and (
                        self.leng - 1) % q == 0:
                    self.period = q
                    j = 1
                    while j <= (self.leng - 1) // q - 1:  # fully repeated
                        k = 0
                        while k <= self.height - 1:
                            binary_7 = '0' * (6 - len(bin(self.lines[k][q]))) + bin(self.lines[k][q])[2:]
                            binary_8 = '0' * (6 - len(bin(self.lines[k][(j + 1) * q]))) + bin(
                                self.lines[k][(j + 1) * q])[2:]
                            if self.lines[k][0: q] != self.lines[k][j * q: (j + 1) * q]:
                                self.period = 0
                            if binary_7[3] != binary_8[3]:
                                self.period = 0
                            k += 1
                        j += 1
                q += 1
            if self.period < 2:
                raise FriezeError('Input does not represent a frieze.')

    def check_vertical(self):
        vertical_lines = copy.deepcopy(self.lines)
        i, count, m = 0, 0, 0
        while i <= len(vertical_lines) - 1:
            j = 0
            while j <= len(vertical_lines[0]) - 1:
                binary_vertical = '0' * (6 - len(bin(self.lines[i][j]))) + bin(self.lines[i][j])[2:]
                if binary_vertical[0] == '1' and i < len(vertical_lines) - 1 and j < len(vertical_lines[0]) - 1:
                    vertical_lines[i + 1][j + 1] += 2
                if binary_vertical[1] == '1' and j < len(vertical_lines[0]) - 1:
                    vertical_lines[i][j + 1] += 4
                if binary_vertical[2] == '1' and i > 0 and j < len(vertical_lines[0]) - 1:
                    vertical_lines[i - 1][j + 1] += 8
                j += 1
            i += 1
        while m <= self.leng - 1:  # avoid period = 2 and only —— |
            n = 0
            while n <= self.height - 1:
                binary_v = '0' * (6 - len(bin(self.lines[n][m]))) + bin(self.lines[n][m])[2:]
                count += 1 if int(binary_v[0]) + int(binary_v[2]) else count
                n += 1
            m += 1
        if count == 0 and self.period == 2:
            return
        j = 0
        while j <= len(vertical_lines[0]) // 2:  # vertical line is in the middle of two points
            if 2 * j - 1 < self.period:
                j += 1
                continue
            if vertical_lines[0][1: j] == (vertical_lines[0][j: 2 * j - 1][::-1]):
                i = 1
                while i <= len(vertical_lines) - 1:
                    if vertical_lines[i][1: j] != vertical_lines[i][j: 2 * j - 1][::-1]:
                        break
                    if i == len(vertical_lines) - 1:
                        self.vertical = 1
                        return
                    i += 1
            j += 1
        p = 3
        while p <= len(vertical_lines[0]) // 2 + 1:  # vertical line is on one point
            if 2 * p - 1 <= self.period:  # two parts should at least be one period
                p += 1
                continue
            if vertical_lines[0][1: p] == (vertical_lines[0][p - 1: 2 * p - 2][::-1]):
                i = 1
                while i <= len(vertical_lines) - 1:
                    if vertical_lines[i][1: j] != vertical_lines[i][p - 1: 2 * p - 2][::-1]:
                        break
                    if i == len(vertical_lines) - 1:
                        self.vertical = 1
                        return
                    i += 1
            p += 1

    def analyse(self):
        # check glided_horizontal
        glided_horizontal = 0
        if self.period % 2 == 0:
            glided_horizontal_lines, i, m, n = copy.deepcopy(self.lines), 0, 0, 0
            while i <= len(glided_horizontal_lines) - 1:
                j = 0
                while j <= len(glided_horizontal_lines[0]) - 1:
                    binary_glided_horizontal = '0' * (6 - len(bin(self.lines[i][j]))) + bin(self.lines[i][j])[2:]
                    if binary_glided_horizontal[0] == '1' and i < len(glided_horizontal_lines) - 1 and j < len(
                            glided_horizontal_lines[0]) - 1:
                        glided_horizontal_lines[i + 1][j + 1] += 8
                    if binary_glided_horizontal[2] == '1' and i != 0 and j < len(glided_horizontal_lines[0]) - 1:
                        glided_horizontal_lines[i][j] += 6
                        glided_horizontal_lines[i - 1][j + 1] += 8
                    if binary_glided_horizontal[3] == '1':
                        glided_horizontal_lines[i][j] += 1
                        glided_horizontal_lines[i - 1][j] += 2
                    j += 1
                i += 1
            list_shift = copy.deepcopy(glided_horizontal_lines[(len(glided_horizontal_lines) + 1) // 2:])
            while m <= len(list_shift) - 1:
                list_shift[-1 - m] = glided_horizontal_lines[m]
                m += 1
            while n <= len(list_shift) - 1:  # compare one period only
                if list_shift[n][1:self.period + 2] != glided_horizontal_lines[n - len(list_shift)][
                                                       self.period // 2 + 1: self.period + 2 + self.period // 2]:
                    break
                if n == len(list_shift) - 1:
                    glided_horizontal = 1
                    break
                n += 1
        else:  # odd period
            glided_horizontal = 0
        self.check_vertical()
        # check rotation
        rotation, rotation_lines, i, rotation_line, comp_list, m, n = 0, copy.deepcopy(self.lines), 0, [], [], 0, 1
        while i <= len(rotation_lines) - 1:
            j = 0
            while j <= len(rotation_lines[0]) - 1:
                binary_rotation = '0' * (6 - len(bin(self.lines[i][j]))) + bin(self.lines[i][j])[2:]
                if binary_rotation[0] == '1' and i < len(rotation_lines) - 1 and j < len(rotation_lines[0]) - 1:
                    rotation_lines[i + 1][j + 1] += 8
                if binary_rotation[1] == '1':
                    rotation_lines[i][j + 1] += 4
                if binary_rotation[2] == '1' and i > 0 and j < len(rotation_lines[0]) - 1:
                    rotation_lines[i - 1][j + 1] += 2
                if binary_rotation[3] == '1':
                    rotation_lines[i - 1][j] += 1
                j += 1
            i += 1
        while m <= len(rotation_lines) - 1:
            rotation_line.append(rotation_lines[-1 - m][1:self.period + 2][::-1])
            m += 1
        while n <= len(rotation_lines[0]) - 1:
            i = 0
            while i <= len(rotation_lines) - 1:
                comp_list.append(rotation_lines[i][n: n + self.period + 1])
                i += 1
            if comp_list != rotation_line:
                comp_list = []
            else:
                rotation = 1
                break
            n += 1
        # check horizontal
        horizontal, horizontal_lines, i = 0, copy.deepcopy(self.lines), 0
        while i <= len(horizontal_lines) - 1:
            j = 0
            while j <= len(horizontal_lines[0]) - 1:
                binary_horizontal = '0' * (6 - len(bin(self.lines[i][j]))) + bin(self.lines[i][j])[2:]
                if binary_horizontal[0] == '1' and i < len(horizontal_lines) - 1 and j < len(horizontal_lines[0]) - 1:
                    horizontal_lines[i + 1][j + 1] += 8
                if binary_horizontal[2] == '1' and i != 0 and j < len(horizontal_lines[0]) - 1:
                    horizontal_lines[i][j] += 6
                    horizontal_lines[i - 1][j + 1] += 8
                if binary_horizontal[3] == '1':
                    horizontal_lines[i][j] += 1
                    horizontal_lines[i - 1][j] += 2
                j += 1
            i += 1
        if (len(horizontal_lines) % 2) == 1:  # horizontal line is on one point
            if horizontal_lines[:len(horizontal_lines) // 2 + 1] == horizontal_lines[
                                                                    -1:len(horizontal_lines) // 2 - 1:-1]:
                horizontal = 1
        else:  # horizontal line is in the middle of two points
            if horizontal_lines[:len(horizontal_lines) // 2] == horizontal_lines[-1:len(horizontal_lines) // 2 - 1:-1]:
                horizontal = 1
        # analyse
        if self.vertical == 1 and glided_horizontal == horizontal == 0:
            print(f'Pattern is a frieze of period {self.period} that is invariant under translation')
            print('        and vertical reflection only.')
        elif horizontal == 1 and self.vertical == 0:
            print(f'Pattern is a frieze of period {self.period} that is invariant under translation')
            print('        and horizontal reflection only.')
        elif glided_horizontal == 1 and self.vertical == 0:
            print(f'Pattern is a frieze of period {self.period} that is invariant under translation')
            print('        and glided horizontal reflection only.')
        elif rotation == 1 and self.vertical == glided_horizontal == 0:
            print(f'Pattern is a frieze of period {self.period} that is invariant under translation')
            print('        and rotation only.')
        elif self.vertical == horizontal == rotation == 1:
            print(f'Pattern is a frieze of period {self.period} that is invariant under translation,')
            print('        horizontal and vertical reflections, and rotation only.')
        elif self.vertical == glided_horizontal == rotation == 1:
            print(f'Pattern is a frieze of period {self.period} that is invariant under translation,')
            print('        glided horizontal and vertical reflections, and rotation only.')
        else:
            print(f'Pattern is a frieze of period {self.period} that is invariant under translation only.')

    def display(self):
        NW_SE, W_E, SW_NE, N_S = [], [], [], []
        i = 0
        while i <= self.leng - 1:
            j = 0
            while j <= self.height - 1:
                binary_N_S = '0' * (6 - len(bin(self.lines[j][i]))) + bin(self.lines[j][i])[2:]
                if binary_N_S[3] == '1':
                    N_S.append(f'{i},{j - 1},{i},{j}')
                j += 1
            i += 1
        j = 0
        while j <= self.height - 1:
            i = 0
            while i <= self.leng - 1:
                binary_W_E = '0' * (6 - len(bin(self.lines[j][i]))) + bin(self.lines[j][i])[2:]
                if binary_W_E[1] == '1':
                    W_E.append(f'{i},{j},{i + 1},{j}')
                i += 1
            j += 1
        m, n = 0, 0
        while n <= self.height + self.leng - 2:
            i = self.leng - 1
            while i >= 0:
                if 0 <= self.leng - i - 1 < self.leng and 0 <= n - i < self.height:
                    binary_NW_SE = '0' * (6 - len(bin(self.lines[n - i][self.leng - i - 1]))) + bin(
                        self.lines[n - i][self.leng - i - 1])[2:]
                    if binary_NW_SE[0] == '1':
                        NW_SE.append(f'{self.leng - i - 1},{n - i},{self.leng - i},{n - i + 1}')
                i -= 1
            n += 1
        while m <= self.height + self.leng - 2:
            i = 0
            while i <= m:
                if i < self.leng and m - i < self.height:
                    binary_SW_NE = '0' * (6 - len(bin(self.lines[m - i][i]))) + bin(self.lines[m - i][i])[2:]
                    if binary_SW_NE[2] == '1':
                        SW_NE.append(f'{i},{m - i},{i + 1},{m - i - 1}')
                i += 1
            m += 1
        W_E_path, run_path, i = [], [], 0
        while i <= len(W_E) - 2:
            if not run_path:
                run_path = W_E[i].split(',')
            if run_path[2:] == W_E[i + 1].split(',')[:2]:
                run_path = run_path[:2] + W_E[i + 1].split(',')[2:]
            else:
                W_E_path.append(run_path)
                run_path = W_E[i + 1].split(',')
            if i == len(W_E) - 2:
                W_E_path.append(run_path)
            i += 1
        N_S_path, run_path, i = [], [], 0
        while i <= len(N_S) - 2:
            if not run_path:
                run_path = N_S[i].split(',')
            if run_path[2:] == N_S[i + 1].split(',')[:2]:
                run_path = run_path[:2] + N_S[i + 1].split(',')[2:]
            else:
                N_S_path.append(run_path)
                run_path = N_S[i + 1].split(',')
            if i == len(N_S) - 2:
                N_S_path.append(run_path)
            i += 1
        SW_NE_path, run_path, i = [], [], 0
        while i <= len(SW_NE) - 2:
            if not run_path:
                run_path = SW_NE[i].split(',')
            if run_path[2:] == SW_NE[i + 1].split(',')[:2]:
                run_path = run_path[:2] + SW_NE[i + 1].split(',')[2:]
            else:
                SW_NE_path.append(run_path)
                run_path = SW_NE[i + 1].split(',')
            if i == len(SW_NE) - 2:
                SW_NE_path.append(run_path)
            i += 1
        NW_SE_path, run_path, i = [], [], 0
        while i <= len(NW_SE) - 2:
            if not run_path:
                run_path = NW_SE[i].split(',')
            if run_path[2:] == NW_SE[i + 1].split(',')[:2]:
                run_path = run_path[:2] + NW_SE[i + 1].split(',')[2:]
            else:
                NW_SE_path.append(run_path)
                run_path = NW_SE[i + 1].split(',')
            if i == len(NW_SE) - 2:
                NW_SE_path.append(run_path)
            i += 1
        W_E_path = sorted(W_E_path, key=lambda x: (int(x[1]), int(x[0])))
        NW_SE_path = sorted(NW_SE_path, key=lambda x: (int(x[1]), int(x[0])))
        N_S_path = sorted(N_S_path, key=lambda x: (int(x[0]), int(x[1])))
        SW_NE_path = sorted(SW_NE_path, key=lambda x: (int(x[1]), int(x[0])))
        filename = self.filename.split('.')[0]
        with open(filename + '.tex', 'w'):
            print(
                '\\documentclass[10pt]{article}\n'
                '\\usepackage{tikz}\n'
                '\\usepackage[margin=0cm]{geometry}\n'
                '\\pagestyle{empty}\n\n'
                '\\begin{document}\n\n'
                '\\vspace*{\\fill}\n'
                '\\begin{center}\n'
                '\\begin{tikzpicture}[x=0.2cm, y=-0.2cm, thick, purple]'
            )
            print('% North to South lines')
            for i in N_S_path:
                print(f'    \\draw ({i[0]},{i[1]}) -- ({i[2]},{i[3]});')
            print('% North-West to South-East lines')
            for i in NW_SE_path:
                print(f'    \\draw ({i[0]},{i[1]}) -- ({i[2]},{i[3]});')
            print('% West to East lines')
            for i in W_E_path:
                print(f'    \\draw ({i[0]},{i[1]}) -- ({i[2]},{i[3]});')
            print('% South-West to North-East lines')
            for i in SW_NE_path:
                print(f'    \\draw ({i[0]},{i[1]}) -- ({i[2]},{i[3]});')
            print(
                '\\end{tikzpicture}\n'
                '\\end{center}\n'
                '\\vspace*{\\fill}\n\n'
                '\\end{document}'
            )


class FriezeError(Exception):
    def __init__(self, message):
        self.message = message
