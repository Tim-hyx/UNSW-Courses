# Written by Eric Martin for COMP9021


from ast import literal_eval


class GaleShapley:
    def __init__(self):
        while True:
            print('Enter a list of n lists, each of which is a '
                  'permutation of {1, ..., m},\nto express the '
                  'preferences of n men for m women:'
                 )
            self.men_preferences = literal_eval(input('    '))
            nb_of_men = len(self.men_preferences)
            nb_of_women = len(self.men_preferences[0])\
                              if self.men_preferences else 0
            if any(set(preferences) != set(range(1, nb_of_women + 1))
                       for preferences in self.men_preferences
                  ):
                print('Your input is incorrect.')
            else:
                break
        while True:
            print(f'Enter a list of {nb_of_women} lists, each of which '
                  f'is a permutation of {{1, ..., {nb_of_men}}},\nto '
                  'express the preferences of the women for the men:'
                 )
            self.women_preferences = literal_eval(input('    '))
            if len(self.women_preferences) != nb_of_women\
               or any(set(preferences) != set(range(1, nb_of_men + 1))
                          for preferences in self.women_preferences
                     ):
                print('Your input is incorrect.')
            else:
                break
        print(f'Optionally input {nb_of_men} names for the men.\n'
              f'In case you do not input {nb_of_men} distinct '
              'strings,\nthen the men will referred to as '
              f'"man 1", ..., "man {nb_of_men}":'
             ) 
        self.men_names = input('    ').split()
        if len(self.men_names) != nb_of_men\
           or len(set(self.men_names)) != nb_of_men:
            self.men_names = [f'man {i}' for i in range(1, nb_of_men + 1)]
        print(f'Optionally input {nb_of_women} names for the women.\n'
              f'In case you do not input {nb_of_women} distinct '
              'strings,\nthen the women will referred to as '
              f'"woman 1", ..., "woman {nb_of_women}":'
             ) 
        self.women_names = input('    ').split()
        if len(self.women_names) != nb_of_women\
           or len(set(self.women_names)) != nb_of_women:
            self.women_names = [f'woman {i}'
                                    for i in range(1, nb_of_women + 1)
                               ]

    def stable_matching(self, men_choosing=True):
        if men_choosing:
            choosers_preferences = self.men_preferences
            accepters_preferences = self.women_preferences
            choosers_names = self.men_names
            accepters_names = self.women_names
        else:
            choosers_preferences = self.women_preferences
            accepters_preferences = self.men_preferences
            choosers_names = self.women_names
            accepters_names = self.men_names
        choosers_preferences = {i: (j - 1 for j in choosers_preferences[i])
                                    for i in range(len(choosers_preferences))
                               }
        accepters_rankings = [{accepters_preferences[i][j] - 1: j
                                  for j in range(len(choosers_preferences))
                              } for i in range(len(accepters_preferences))
                             ]
        free_choosers = list(choosers_preferences)
        acceptances = {}
        while free_choosers:
            try:
                chooser = free_choosers.pop()
                accepter = next(choosers_preferences[chooser])
                if accepter not in acceptances:
                    acceptances[accepter] = chooser
                elif accepters_rankings[accepter][chooser] <\
                        accepters_rankings[accepter][acceptances[accepter]]:
                    free_choosers.append(acceptances[accepter])
                    acceptances[accepter] = chooser
                else:
                    free_choosers.append(chooser)
            except StopIteration:
                pass
        solution = {acceptances[accepter]: accepter for accepter in acceptances}
        print('The matches are:')
        for chooser in sorted(solution, key=lambda x: choosers_names[x]):
            print(choosers_names[chooser], '\u26ad',
                  accepters_names[solution[chooser]]
                 )
