class ProtectedSection:
    """Handle exceptions gracefully within a given section"""

    def __init__(self, log = (), suppress = ()):
        self.log = log
        self.suppress = suppress
        self.exception = None

    def __enter__(self):
        self.exception = None
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is None:
            return True
        if isinstance(exc_val, self.log):
            self.exception = exc_val
            return True
        if isinstance(exc_val, self.suppress):
            return True
        return False
