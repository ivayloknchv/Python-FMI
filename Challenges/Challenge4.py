class LockPicker_2MI0600305:

    def __init__(self, lock):
        self.lock = lock

    def unlock(self):

        valid_args = []

        while True:
            try:
                if self.lock.pick(*valid_args):
                    return True
            except TypeError as err:
                if err.position is None:
                    valid_args.extend([None] * err.expected)
                elif isinstance(err.position, int):
                   valid_args[err.position - 1] = err.expected()
            except ValueError as err:
                   valid_args[err.position - 1] = err.expected
