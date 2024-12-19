class Squarer:

    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    def __iter__(self):
        return SquarerIterator(self.begin, self.end)

#iterator
class SquarerIterator:

    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.begin <= self.end:
            ans = self.begin ** 2
            self.begin += 1
            return ans
        else:
            raise StopIteration

#generator
def squarer_generator(begin, end):
    current = begin
    while current <= end:
        yield  current ** 2
        current += 1
