class MultidimensionalArray:
    """Create and manage 0-index multidimensional array"""

    def __init__(self, dim_sizes):
        self.dim_sizes = dim_sizes
        self.data = self._allocate_data(self.dim_sizes)

    def _validate_coordinates_vector(self, coordinates_vector):
        expr = any(not (0 <= coordinates_vector[i] < self.dim_sizes[i]) for i in range(0, len(coordinates_vector)))
        return not expr

    def _allocate_data(self, dim_sizes, depth = 0):
        """Recursively allocate a multidimensional array filled with zeros"""
        if depth == len(self.dim_sizes) - 1:
            to_return  = [0] * self.dim_sizes[depth]
            return  to_return

        to_return = []
        for i in range(0, dim_sizes[depth]):
            to_return.append(self._allocate_data(dim_sizes, depth + 1))
        return to_return

    @staticmethod
    def _get_element(elements, coordinates, depth = 0):
        if depth == len(coordinates) - 1:
            return elements[coordinates[depth]]
        return MultidimensionalArray._get_element(elements[coordinates[depth]], coordinates, depth+1)

    def __getitem__(self, coordinates):
        """Return a single element or a whole subarray at a given position"""

        if len(coordinates) > len(self.dim_sizes) or not self._validate_coordinates_vector(coordinates):
            raise IndexError("Trying to access invalid index!")
        return self._get_element(self.data, coordinates)

    @staticmethod
    def _set_element(elements, coordinates, value, depth = 0):
        if depth == len(coordinates) - 1:
            elements[coordinates[depth]] = value
            return
        MultidimensionalArray._set_element(elements[coordinates[depth]], coordinates, value, depth+1)

    def __setitem__(self, coordinates, value):
        """Set an element at a given position"""

        if len(coordinates) != len(self.dim_sizes) or not self._validate_coordinates_vector(coordinates):
            raise IndexError("Trying to access invalid index!")
        self._set_element(self.data, coordinates, value)



class AddFunction:
    """Simulate addition of numbers"""

    _VALID_TYPES = (int, float)

    def __init__(self, num):
        self.num = num

    def __call__(self, val):
        if isinstance(val, self._VALID_TYPES):
            self.num += val
        return self

    def __add__ (self, other):
        if isinstance(other, self._VALID_TYPES):
            return self.num + other

    def __str__(self):
        return f'{self.num}'
