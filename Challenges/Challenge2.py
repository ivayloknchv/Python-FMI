SPOOKY_PREFIX = 'spooky_'

class HauntedMansion:
    """Make everything spooky."""

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.__setattr__(key,value)

    def __setattr__(self, key, value):
        spooky_key = SPOOKY_PREFIX + key
        object.__setattr__(self, spooky_key, value)

    def __getattr__(self, item):
        return 'Booooo, only ghosts here!'
