# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION
#
# Creates a class to represent a permutation of 1, 2, ..., n for some n >= 0.
#
# An object is created by passing as argument to the class name:
# - either no argument, in which case the empty permutation is created, or
# - "length = n" for some n >= 0, in which case the identity over 1, ..., n
#   is created, or
# - the numbers 1, 2, ..., n for some n >= 0, in some order, possibly together
#   with "lengh = n".
#
# __len__(), __repr__() and __str__() are implemented, the latter providing
# the standard form decomposition of the permutation into cycles
# (see wikepedia page on permutations for details).
# - A given cycle starts with the largest value in the cycle.
# - Cycles are given from smallest first value to largest first value.
#
# Objects have:
# - nb_of_cycles as an attribute
# - inverse() as a method
#
# The * operator is implemented for permutation composition, for both infix
# and in-place uses.
from collections import defaultdict


class PermutationError(Exception):
    def __init__(self, message):
        self.message = message


class Permutation:
    def __init__(self, *args, length=None):
        global test_set
        i, k, j, self.dict = 0, 0, 0, defaultdict()
        while i <= len(args) - 1:
            if not isinstance(args[i], int):
                raise PermutationError('Cannot generate permutation from these arguments')
            i += 1
        if len(args) > 0:
            test_set, m = set(), 1
            while m <= max(args):
                test_set.add(m)
                m += 1
        args_set = set(args)
        if len(args) == 0 and length is None:
            self.args = args
        elif len(args) == 0 and length is not None and length > 0:
            self.args, n = [], 1
            while n <= length:
                self.args.append(n)
                n += 1
            self.args = tuple(self.args)
        elif len(args) > 0 and (
                (length is not None and length == len(args_set)) or (length is None)) and args_set == test_set:
            self.args = args
        else:
            raise PermutationError('Cannot generate permutation from these arguments')
        while k <= len(self.args) - 1:
            self.dict[k + 1] = self.args[k]
            k += 1
        run_list, self.circle, used_set = [], [], set()
        if len(self.dict) > 0:
            i = 1
            run_list.append(i)
            used_set = used_set.union({i})
            while True:
                if self.dict[i] == run_list[0]:
                    self.circle.append(run_list)
                    used_set = used_set.union(set(run_list))
                    run_list = []
                    for key in self.dict.keys():
                        if key not in used_set:
                            i = key
                            run_list.append(i)
                            break
                else:
                    run_list.append(self.dict[i])
                    i = self.dict[i]
                if len(used_set) == len(self.dict):
                    break
        else:
            pass
        while j <= len(self.circle) - 1:
            a = self.circle[j][self.circle[j].index(max(self.circle[j])):]
            b = self.circle[j][0: self.circle[j].index(max(self.circle[j]))]
            self.circle[j] = a + b
            j += 1
        self.circle, self.nb_of_cycles = sorted(self.circle, key=lambda x: x[0]), len(self.circle)
        # Replace pass above with your code

    def __len__(self):
        return len(self.args)
        # Replace pass above with your code

    def __repr__(self):
        return f'Permutation{self.args}'
        # Replace pass above with your code

    def __str__(self):
        if len(self.circle) != 0:
            result, i = '', 0
            while i <= len(self.circle) - 1:
                result += '('
                j = 0
                while j <= len(self.circle[i]) - 1:
                    result += str(self.circle[i][j])
                    if self.circle[i][j] != self.circle[i][-1]:
                        result += ' '
                    j += 1
                result += ')'
                i += 1
        else:
            result = '()'
        return f'{result}'

    # Replace pass above with your code

    def __mul__(self, permutation):
        mul_tuple = []
        if len(self.dict) != len(permutation.dict):
            raise PermutationError('Cannot compose permutations of different lengths')
        elif len(self.dict) == len(permutation.dict) > 0:
            for key in self.dict.keys():
                mul_tuple.append(permutation.dict[self.dict[key]])
            mul_tuple = tuple(mul_tuple)
            return Permutation(*mul_tuple)
        else:
            return Permutation()
        # Replace pass above with your code

    def __imul__(self, permutation):
        imul_tuple = []
        if len(self.dict) != len(permutation.dict):
            raise PermutationError('Cannot compose permutations of different lengths')
        elif len(self.dict) == len(permutation.dict) > 0:
            for key in self.dict.keys():
                imul_tuple.append(permutation.dict[self.dict[key]])
            imul_tuple = tuple(imul_tuple)
            return Permutation(*imul_tuple)
        else:
            return Permutation()
        # Replace pass above with your code

    def inverse(self):
        result = []
        if len(self.dict) > 0:
            i = 0
            while i <= len(self.dict) - 1:
                for j in self.dict.keys():
                    if self.dict[j] == i + 1:
                        result.append(j)
                        break
                i += 1
        result = tuple(result)
        return Permutation(*result)
        # Replace pass above with your code

    # Insert helper functions, if needed
