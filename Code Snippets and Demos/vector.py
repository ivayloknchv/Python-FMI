class Vector:

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z


    def _coordinates(self):
        return self._x, self._y, self._z


    @property
    def length(self):
        return sum(_ ** 2 for _ in self._coordinates()) ** 0.5


    @property
    def x(self):
        return self._x


    @property
    def y(self):
        return self._y


    @property
    def z(self):
        return self._z


    @x.setter
    def x(self, new_x):
        self._x = new_x


    @y.setter
    def y(self, new_y):
        self._y = new_y


    @z.setter
    def z(self, new_z):
        self._z = new_z


    def normalize(self):
        vector_length = self.length
        self._x /=  vector_length
        self._y /=  vector_length
        self._z /=  vector_length


    def normalized(self):
        vector_length = self.length
        norm_x = self._x / vector_length
        norm_y = self._y / vector_length
        norm_z = self._z / vector_length
        return Vector(norm_x, norm_y, norm_z)


    def print_vector(self):
        print(f'({self._x}, {self._y}, {self._z})')


    def __iadd__(self, other):
        self._x += other.x
        self._y += other.y
        self._z += other.z
        return self


    def __add__(self, other):
        new_x = self._x + other.x
        new_y = self._y + other.y
        new_z = self._z + other.z
        return  Vector(new_x, new_y, new_z)

    def __isub__(self, other):
        self._x -= other.x
        self._y -= other.y
        self._z -= other.z
        return self


    def __sub__(self, other):
        new_x = self._x - other.x
        new_y = self._y - other.y
        new_z = self._z - other.z
        return  Vector(new_x, new_y, new_z)


    def __imul__(self, scalar):
        self._x *= scalar
        self._y *= scalar
        self._z *= scalar
        return self


    def __mul__(self, scalar):
        new_x = self._x * scalar
        new_y = self._y * scalar
        new_z = self._z * scalar
        return Vector(new_x, new_y, new_z)


    def __rmul__(self, scalar):
        return self.__mul__(scalar)
