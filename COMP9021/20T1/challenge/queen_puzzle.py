# Written by Eric Martin for COMP9021


class QueenPuzzle:
    def __init__(self, board_size):
        self.board_size = board_size
        self.nb_of_solutions = 0
        self.nb_of_tested_permutations = 0
        self._solutions = []
        self._solve_puzzle()

    def solution(self, k):
        k -= 1
        cells = {0: '\N{White Large Square}', 1: '\N{Black Large Square}'}
        queens = {0: '\N{Large Red Circle}', 1: '\N{Large Blue Circle}'}
        for i in range(self.board_size):
            for j in range(self.board_size):
                black_or_white = (i + j) % 2
                print(j == self._solutions[k][i] and queens[black_or_white]
                      or cells[black_or_white], end=''
                     )
            print()

    def _solve_puzzle(self):
        self._L = list(range(self.board_size))
        for is_solution in self._heap_permute(self.board_size):
            self.nb_of_tested_permutations += 1
            if is_solution:
                self.nb_of_solutions += 1
                self._solutions.append(list(self._L))

    def _heap_permute(self, length):
        if length == 1:
            yield not self._attacks_queen_below()
        else:
            length -= 1
            for i in range(length):
                yield from self._heap_permute_below(length)
                if length % 2:
                    self._L[i], self._L[length] = self._L[length], self._L[i]
                else:
                    self._L[0], self._L[length] = self._L[length], self._L[0]
            yield from self._heap_permute_below(length)

    def _heap_permute_below(self, length):
        for is_solution in self._heap_permute(length):
            if self._attacks_queen_below(length):
                yield False
                if length > 1:
                    self._skip_permutations(length)
                break
            yield is_solution

    def _skip_permutations(self, skip_size):
        if skip_size % 2 or skip_size == 2:
           self._L[0], self._L[skip_size - 1] =\
                   self._L[skip_size - 1], self._L[0]
        elif skip_size == 4:
            self._L[: 3], self._L[3] = self._L[1 : 4], self._L[0]
        else:
            self._L[: 2], self._L[2 : skip_size - 2],\
             self._L[skip_size - 2], self._L[skip_size - 1] =\
                    self._L[skip_size - 3 : skip_size - 1],\
                     self._L[1 : skip_size - 3],\
                      self._L[skip_size - 1], self._L[0]

    def _attacks_queen_below(self, n=0):
        # Returns True iff the queen on the (n+1)th row attacks
        # a queen on a lower row.
        return any(abs(self._L[i] - self._L[n]) == i - n
                       for i in range(n + 1, self.board_size)
                  )
