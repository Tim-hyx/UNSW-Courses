from copy import copy
from itertools import combinations


class DiffCommandLine:
    def __init__(self, every_line):
        self.left_1, self.left_2, self.right_1, self.right_2, self.action = None, None, None, None, None
        self.every_line = every_line.strip()
        actions = ['d', 'a', 'c']
        judge = True
        if ' ' in every_line:
            judge = False
            if judge == False:
                raise DiffCommandsError()
        i = 0
        while i < len(actions):
            action = actions[i]
            if action in every_line:
                read_numbers = every_line.strip()
                read_numbers = read_numbers.split(action)
                right_numbers, left_numbers = read_numbers[1], read_numbers[0]
                if right_numbers.isspace() == True:
                    judge = False
                    if judge == False:
                        raise DiffCommandsError()
                if left_numbers.isspace() == True:
                    judge = False
                    if judge == False:
                        raise DiffCommandsError()
                right_number_list, left_number_list = right_numbers.split(','), left_numbers.split(',')
                k = 0
                while k < len(right_number_list):
                    number = right_number_list[k]
                    if number.isdigit() == True:
                        if int(number) != abs(int(number)):
                            judge = False
                            if judge == False:
                                raise DiffCommandsError()
                    if number.isdigit() == False:
                        judge = False
                        if judge == False:
                            raise DiffCommandsError()
                    k += 1
                j = 0
                while j < len(left_number_list):
                    number = left_number_list[j]
                    if number.isdigit() == True:
                        if int(number) != abs(int(number)):
                            judge = False
                            if judge == False:
                                raise DiffCommandsError()
                    if number.isdigit() == False:
                        judge = False
                        if judge == False:
                            raise DiffCommandsError()
                    j += 1
                if action == 'c':
                    if len(left_number_list) == 1 and len(right_number_list) == 1:
                        self.right_2 = int(right_number_list[0])
                        self.right_1 = self.right_2 - 1
                        self.left_2 = int(left_number_list[0])
                        self.left_1 = self.left_2 - 1
                    elif len(left_number_list) == 2 and len(right_number_list) == 2:
                        self.right_1, self.right_2 = int(right_number_list[0]) - 1, int(right_number_list[1])
                        self.left_1, self.left_2 = int(left_number_list[0]) - 1, int(left_number_list[1])
                    elif len(left_number_list) == 1 and len(right_number_list) == 2:
                        self.right_1, self.right_2 = int(right_number_list[0]) - 1, int(right_number_list[1])
                        self.left_2 = int(left_number_list[0])
                        self.left_1 = self.left_2 - 1
                    elif len(left_number_list) == 2 and len(right_number_list) == 1:
                        self.right_2 = int(right_number_list[0])
                        self.right_1 = self.right_2 - 1
                        self.left_1, self.left_2 = int(left_number_list[0]) - 1, int(left_number_list[1])
                    else:
                        judge = False
                        if judge == False:
                            raise DiffCommandsError()
                elif action == 'd':
                    if len(left_number_list) == 2 and len(right_number_list) == 1:
                        self.right_1 = int(right_number_list[0])
                        self.right_2 = self.right_1
                        self.left_1, self.left_2 = int(left_number_list[0]) - 1, int(left_number_list[1])
                    elif len(left_number_list) == 1 and len(right_number_list) == 1:
                        self.right_1, self.right_2 = int(right_number_list[0]), int(right_number_list[0])
                        self.left_2 = int(left_number_list[0])
                        self.left_1 = self.left_2 - 1
                    else:
                        judge = False
                        if judge == False:
                            raise DiffCommandsError()
                elif action == 'a':
                    if len(left_number_list) == 1 and len(right_number_list) == 2:
                        self.right_1, self.right_2 = int(right_number_list[0]) - 1, int(right_number_list[1])
                        self.left_1 = int(left_number_list[0])
                        self.left_2 = self.left_1
                    elif len(left_number_list) == 1 and len(right_number_list) == 1:
                        self.right_2, self.right_1 = int(right_number_list[0]), int(right_number_list[0]) - 1
                        self.left_1, self.left_2 = int(left_number_list[0]), int(left_number_list[0])
                    else:
                        judge = False
                        if judge == False:
                            raise DiffCommandsError()
                self.action = action
                if self.right_2 < self.right_1:
                    judge = False
                    if judge == False:
                        raise DiffCommandsError()
                if self.left_1 == 0 and self.right_1 != 0:
                    judge = False
                    if judge == False:
                        raise DiffCommandsError()
                if self.left_2 < self.left_1:
                    judge = False
                    if judge == False:
                        raise DiffCommandsError()
                if judge == False:
                    raise DiffCommandsError()
                break
            i += 1
        else:
            judge = False
            if judge == False:
                raise DiffCommandsError()


class DiffCommands:
    def __init__(self, file=None):
        self.file_lines, self.command_lines = [], []
        judge = True
        if file is not None:
            with open(file) as open_file:
                for line in open_file:
                    command_line = DiffCommandLine(line)
                    self.command_lines.append(command_line)
                    self.file_lines.append(line.strip())
        if self.command_lines:
            first_line = self.command_lines[0]
            for second_line in self.command_lines[1:]:
                if second_line.left_1 - first_line.left_2 != second_line.right_1 - first_line.right_2:
                    judge = False
                    if judge == False:
                        raise DiffCommandsError()
                if second_line.left_1 == first_line.left_2:
                    judge = False
                    if judge == False:
                        raise DiffCommandsError()
                if second_line.right_1 == first_line.right_2:
                    judge = False
                    if judge == False:
                        raise DiffCommandsError()
                first_line = second_line
        if judge == False:
            raise DiffCommandsError()

    def __str__(self):
        a = "\n".join(self.file_lines)
        b = a.strip()
        return b


class DiffCommandsError(Exception):
    def __str__(self):
        return "Cannot possibly be the commands for the diff of two files"


class OriginalNewFiles:
    def __init__(self, file1, file2):
        with open(file2, 'r') as open_file:
            self.right_file_lines = [line.strip() for line in open_file if not line.isspace()]
        with open(file1, 'r') as open_file:
            self.left_file_lines = [line.strip() for line in open_file if not line.isspace()]

    def is_a_possible_diff(self, diffCommands):
        left_file_lines, right_file_lines = copy(self.left_file_lines), copy(self.right_file_lines)
        if diffCommands is not None:
            i = 0
            while i < len(diffCommands.command_lines):
                step = diffCommands.command_lines[i]
                if step.left_1 > len(left_file_lines):
                    return False
                if step.left_2 > len(left_file_lines):
                    return False
                if step.right_1 > len(right_file_lines):
                    return False
                if step.right_2 > len(right_file_lines):
                    return False
                if step.action == 'd':
                    index = step.left_1
                    while index < step.left_2:
                        left_file_lines[index] = '...'
                        index += 1
                elif step.action == 'c':
                    index = step.right_1
                    while index < step.right_2:
                        right_file_lines[index] = '...'
                        index += 1
                    index = step.left_1
                    while index < step.left_2:
                        left_file_lines[index] = '...'
                        index += 1
                elif step.action == 'a':
                    index = step.right_1
                    while index < step.right_2:
                        right_file_lines[index] = '...'
                        index += 1
                i += 1
            right_file_line = []
            j = 0
            while j < len(right_file_lines):
                item = right_file_lines[j]
                if item != '...':
                    right_file_line.append(item)
                j += 1
            left_file_line = []
            i = 0
            while i < len(left_file_lines):
                item = left_file_lines[i]
                if item != '...':
                    left_file_line.append(item)
                i += 1
            if left_file_line > right_file_line:
                return False
            if left_file_line < right_file_line:
                return False
            else:
                return True
        return False

    def output_diff(self, diffCommands):
        if self.is_a_possible_diff(diffCommands) == True:
            i = 0
            while i < len(diffCommands.command_lines):
                step = diffCommands.command_lines[i]
                print(step.every_line)
                if step.action == 'd':
                    index = step.left_1
                    while index < step.left_2:
                        print('< ' + self.left_file_lines[index])
                        index += 1
                elif step.action == 'c':
                    index = step.left_1
                    while index < step.left_2:
                        print('< ' + self.left_file_lines[index])
                        index += 1
                    print("---")
                    index = step.right_1
                    while index < step.right_2:
                        print('> ' + self.right_file_lines[index])
                        index += 1
                elif step.action == 'a':
                    index = step.right_1
                    while index < step.right_2:
                        print('> ' + self.right_file_lines[index])
                        index += 1
                i += 1

    def output_unmodified_from_original(self, diffCommands):
        left_file_lines = copy(self.left_file_lines)
        if self.is_a_possible_diff(diffCommands) == True:
            i = 0
            while i < len(diffCommands.command_lines):
                step = diffCommands.command_lines[i]
                if step.action == 'c':
                    index = step.left_1
                    while index < step.left_2:
                        left_file_lines[index] = '...'
                        index += 1
                elif step.action == 'd':
                    index = step.left_1
                    while index < step.left_2:
                        left_file_lines[index] = '...'
                        index += 1
                i += 1
            first = left_file_lines[0]
            print(first)
            for second in left_file_lines[1:]:
                if first != '...' or second != '...':
                    print(second)
                else:
                    pass
                first = second

    def output_unmodified_from_new(self, diffCommands):
        right_file_lines = copy(self.right_file_lines)
        if self.is_a_possible_diff(diffCommands) == True:
            i = 0
            while i < len(diffCommands.command_lines):
                command = diffCommands.command_lines[i]
                if command.action == 'c':
                    index = command.right_1
                    while index < command.right_2:
                        right_file_lines[index] = '...'
                        index += 1
                elif command.action == 'a':
                    index = command.right_1
                    while index < command.right_2:
                        right_file_lines[index] = '...'
                        index += 1
                i += 1
            first = right_file_lines[0]
            print(first)
            for second in right_file_lines[1:]:
                if first != '...' or second != '...':
                    print(second)
                else:
                    pass
                first = second

    def get(self, first_line, second_line):
        if first_line > second_line:
            return f"{first_line},{second_line}"
        if first_line < second_line:
            return f"{first_line},{second_line}"
        else:
            return f"{second_line}"

    def get_all_diff_commands(self):
        if self.left_file_lines == self.right_file_lines:
            return [DiffCommands()]
        m, n = len(self.left_file_lines) + 1, len(self.right_file_lines) + 1
        lcs = [[0 for _ in range(n)] for _ in range(m)]
        point_list = []
        i = 1
        while i < len(lcs):
            j = 1
            while j < len(lcs[0]):
                left_lines, right_lines = self.left_file_lines[i - 1], self.right_file_lines[j - 1]
                if left_lines > right_lines or left_lines < right_lines:
                    lcs[i][j] = max(lcs[i][j - 1], lcs[i - 1][j])
                else:
                    lcs[i][j] = lcs[i - 1][j - 1] + 1
                    point_list.append((i, j, lcs[i][j]))
                j += 1
            i += 1
        max_value = point_list[-1][-1]
        all_commands = combinations(point_list, max_value)
        result = []
        for commands in all_commands:
            first_line = commands[0]
            for second_line in commands[1:]:
                if second_line[0] < first_line[0]:
                    break
                if second_line[1] < first_line[1]:
                    break
                if second_line[2] <= first_line[2]:
                    break
                first_line = second_line
            else:
                result.append(commands)
        diffs = []
        k = 0
        while k < len(result):
            method = result[k]
            diff = DiffCommands()
            diff_left, diff_right = [], []
            i = 0
            while i < len(method):
                diff_right.append(method[i][1])
                diff_left.append(method[i][0])
                i += 1
            diff_left.append(len(self.left_file_lines) + 1)
            diff_right.append(len(self.right_file_lines) + 1)
            left_1 = 0
            right_1 = 0
            for left_2, right_2 in zip(diff_left, diff_right):
                if left_2 > left_1 + 1 and right_2 == right_1 + 1:
                    right_lines, left_lines = self.get(right_1, right_2 - 1), self.get(left_1 + 1, left_2 - 1)
                    diff.file_lines.append(left_lines + 'd' + right_lines)
                elif left_2 == left_1 + 1 and right_2 > right_1 + 1:
                    right_lines, left_lines = self.get(right_1 + 1, right_2 - 1), self.get(left_1, left_2 - 1)
                    diff.file_lines.append(left_lines + 'a' + right_lines)
                elif left_2 > left_1 + 1 and right_2 > right_1 + 1:
                    right_lines, left_lines = self.get(right_1 + 1, right_2 - 1), self.get(left_1 + 1, left_2 - 1)
                    diff.file_lines.append(left_lines + 'c' + right_lines)
                left_1 = left_2
                right_1 = right_2
            diffs.append(diff)
            k += 1
        diffs.sort(key=lambda x: x.file_lines)
        return diffs
    # REPLACE PASS ABOVE WITH YOUR CODE
