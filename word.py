
class Word(str):
    '''The Word class inherits from the str class.
    Which means it gets everything from the str
    class plus whatever it defines. So we will
    redefine >, <, >=, <= so that a Word is
    compared by length, not alphabetically.
    '''

    def __gt__(self, other):
        print('borch gt')
        return len(self) > len(other)
    def __lt__(self, other):
        print('borch lt')
        return len(self) < len(other)
    def __ge__(self, other):
        print('borch ge')
        return len(self) >= len(other)
    def __le__(self, other):
        print('borch le')
        return len(self) <= len(other)
    def __eq__(self, other):
        print('borch eq')
        return len(self) == len(other)
