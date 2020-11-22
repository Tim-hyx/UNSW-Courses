# Written by Eric Martin for COMP9021


from random import choice, seed, shuffle
from collections import defaultdict


class TargetPuzzle:
    def __init__(self, target='', *, minimal_length=4,
                 dictionary='dictionary.txt' 
                ):
        self.dictionary = dictionary
        self.minimal_length = minimal_length
        with open(self.dictionary) as lexicon:
            # A dictionary whose keys are all words consisting of
            # distinct letters; the value for a given key is the set
            # of characters that occur in the key (word), to avoid
            # computing the latter from the former more than once,
            # which is useful only when change_target() is called.
            self.words = dict(filter(lambda x: len(x[0]) == len(x[1]),
                                     ((word, set(word))
                                          for word in (line.rstrip()
                                                           for line in lexicon
                                                      )
                                     )
                                    )
                             )
        self.targets_letters = [self.words[word] for word in self.words
                                                     if len(word) == 9
                               ]
        if len(target) != 9 or set(target) not in self.targets_letters:
            print(repr(target), 'is not a valid target, '
                                'a random one will be generated instead.\n'
                 )
            seed(sum(ord(target[i]) * 128 ** i for i in range(len(target))))
            self.target_letters = choice(self.targets_letters)
            sorted_target_letters = sorted(self.target_letters)
            shuffle(sorted_target_letters)
            self.target = ''.join(sorted_target_letters)
        else:
            self.target = target
            self.target_letters = set(target)
        self._solutions = self._solve_target()

    def __repr__(self):
        return f'Target(target={self.target}, *, '\
               f'minimal_length={self.minimal_length}, '\
               f'dictionary={self.dictionary})'
       
    def __str__(self):
        return '\n'.join(' '.join(self.target[i + j] for j in range(3))
                             for i in range(3)
                        )

    def _solve_target(self):   
        solutions = defaultdict(list)
        for word in self.words:
            if self.minimal_length <= len(word)\
               and self.target[4] in self.words[word]\
               and self.words[word] <= self.target_letters:
                solutions[len(word)].append(word)
        return solutions

    def nb_of_solutions(self):
        print('In decreasing order of length between 9 and',
              f'{self.minimal_length}:'
             )
        for length in range(9, self.minimal_length - 1, -1):
            nb_of_solutions = len(self._solutions[length])
            if nb_of_solutions == 1:
                print(f'    1 solution of length {length}.')
            elif nb_of_solutions > 1:
                print(f'    {nb_of_solutions} solutions of length {length}.')

    def solutions(self, minimal_length=None):
        if minimal_length is None:
            minimal_length = self.minimal_length
        for length in range(9, minimal_length - 1, -1):
            if not self._solutions[length]:
                continue
            if len(self._solutions[length]) == 1:
                print(f'Solution of length {length}:')
            else:               
                print(f'Solutions of length {length}:')
            for solution in self._solutions[length]:
                print('   ', solution)

    def change_letters(self, to_be_replaced, to_replace):
        if len(to_be_replaced) == len(to_replace)\
           and to_be_replaced != to_replace:
            letters_to_be_replaced = set(to_be_replaced)
            if letters_to_be_replaced <= self.target_letters:
                new_target_letters =\
                 self.target_letters - letters_to_be_replaced | set(to_replace)
                if new_target_letters in self.targets_letters:
                    old_target_letters = self.target_letters
                    old_letter_at_centre = self.target[4]
                    self.target_letters = new_target_letters
                    self.target =\
                            self.target.translate(str.maketrans(to_be_replaced,
                                                                to_replace
                                                               )
                                                 )
                    if self.target_letters != old_target_letters\
                       or self.target[4] != old_letter_at_centre:
                        self._solutions = self._solve_target()
                    else:
                        print('The solutions remain the same for sure.')
                    return
        print('The target was not changed.')
