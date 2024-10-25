class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


    def _coordinates(self):
        return self.x, self.y, self.z


    @property
    def length(self):
        return sum(_ ** 2 for _ in self._coordinates()) ** 0.5


    def normalize(self):
        vector_length = self.length
        self.x /=  vector_length
        self.y /=  vector_length
        self.z /=  vector_length


    def normalized(self):
        vector_length = self.length
        norm_x = self.x / vector_length
        norm_y = self.y / vector_length
        norm_z = self.z / vector_length
        return Vector(norm_x, norm_y, norm_z)


    def print_vector(self):
        print(f'({self.x}, {self.y}, {self.z})')


    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self


    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        new_z = self.z + other.z
        return  Vector(new_x, new_y, new_z)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self


    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        new_z = self.z - other.z
        return  Vector(new_x, new_y, new_z)


    def __imul__(self, scalar):
        self.x *= scalar
        self.y *= scalar
        self.z *= scalar
        return self


    def __mul__(self, scalar):
        new_x = self.x * scalar
        new_y = self.y * scalar
        new_z = self.z * scalar
        return Vector(new_x, new_y, new_z)


    def __rmul__(self, scalar):
        return self.__mul__(scalar)
