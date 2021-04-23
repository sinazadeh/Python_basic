class SuperDict(dict):
    fallback_value = "No such key"
    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except KeyError:
            return self.fallback_value

class PlusList(list):
    def __add__(self, value):
        try:
            super().__add__(value)
        except TypeError:
            self.append(value)

class SortedList(PlusList):
    def append(self, value):
        super().append(value)
        self.sort()

class ReversedList(PlusList): 
    def append(self, value):
        super().append(value)
        self.reverse()

class RevSortedList(PlusList):
    def append(self, value):
        super().append(value)
        self.sort()
        self.reverse()

        