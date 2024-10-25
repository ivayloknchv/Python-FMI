class Countable:

    _count = 0

    def __init__(self, x):
        self.x = x
        type(self).increase_count()


    @classmethod
    def increase_count(cls):
        cls._count += 1


    @classmethod
    def decrease_count(cls):
        cls._count -= 1


    def __del__(self):
        type(self).decrease_count()
