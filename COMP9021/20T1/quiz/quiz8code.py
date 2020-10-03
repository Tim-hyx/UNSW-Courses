# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION


# Assignments to a CircularList object will only involve integer indexes.
#
# When the index is an integer, it is interpreted modulo the length
# of the list.
#
# When working with slices:
# - The last argument of a slice cannot be equal to 0.
# - When the last argument of a slice is not given, it is set to 1.
# - When the first argument of a slice is not given, it is set to
#   0 or to -1 depending on the sign of the last argument.
# - When the second argument of a slice is not given, it is set to
#   len(list) or to -len(list) -1 depending on the sign of the last argument.
# - Denoting by L the CircularList object, returns a list consisting of
#   all elements of the form L[i modulo len(L)] for i ranging between first
#   (included) and second (excluded) arguments of slice, in steps given by
#   third argument of slice.

class CircularList:
    def __init__(self, *args):
        self.list = []
        if args is not None:
            i = 0
            while i < len(args):
                self.list.append(args[i])
                i += 1

    def __str__(self):
        empty = []
        i = 0
        while i < len(self.list):
            string = str(self.list[i])
            empty.append(string)
            i += 1
        empty = ', '.join(empty)
        return f'[{empty}]'

    def __len__(self):
        return len(self.list)

    def __setitem__(self, key, value):
        if self.list is not None:
            index = key % len(self.list)
            self.list[index] = value

    def __getitem__(self, item):
        if self.list is not None:
            if isinstance(item, int) == False:
                stop = item.stop
                start = item.start
                step = item.step
                if step is not None:
                    if step == 0:
                        judge = False
                        if not judge:
                            raise ValueError()
                if step is None:
                    step = 1
                if start is None and step <= 0:
                    start = -1
                if start is None and step > 0:
                    start = 0
                if stop is None and step <= 0:
                    stop = -(len(self.list) + 1)
                if stop is None and step > 0:
                    stop = len(self.list)
                final_list = []
                for index in range(start, stop, step):
                    i = index % len(self.list)
                    final_list.append(self.list[i])
                return final_list
            else:
                index = item % len(self.list)
                return self.list[index]


class ValueError(Exception):
    def __str__(self):
        return "slice step cannot be zero"
    # REPLACE PASS ABOVE WITH YOUR CODE
