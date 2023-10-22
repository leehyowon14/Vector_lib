from math import sqrt

def __is_real_number(num):
        if isinstance(num, float) or isinstance(num, int):
            return True
        else:
            return False

class Vector2:
    def __init__(self, x: float | None, y: float | None) -> None:
        if type(x) != float or type(y) != float:
            raise Exception("The component of Vector must be a float")

        self.__x = 0.0 if not x else x
        self.__y = 0.0 if not y else y

    @property
    def x(self) -> float:
        return self.__x

    @property
    def y(self) -> float:
        return self.__y
    
    @x.setter
    def x(self, value: float) -> None:
        self.__x = value

    @y.setter
    def y(self, value: float) -> None:
        self.__y = value
    
    def norm(self) -> float:
        return sqrt(self.__x**2 + self.__y**2)
    
    def normalize(self) -> 'Vector2':
        __norm = self.norm
        return Vector2(self.__x/__norm, self.__y/__norm)
    
    def to_3d(self) -> 'Vector3':
        return Vector3(self.__x, self.__y, 0.0)

    def get_components(self) -> list['Vector2']:
        return [Vector2(self.__x, 0.0), Vector2(0.0, self.__y)]

    def __add__(self, other: 'Vector2') -> 'Vector2':
        if type(self) != type(other):
            if __is_real_number(other):
                return Vector2(self.__x + other, self.__y + other)
            raise Exception("Operations cannot be performed with vectors of other dimensions.")
        return Vector2(self.__x + other.x, self.__y + other.y)
    
    def __sub__(self, other: 'Vector2') -> 'Vector2':
        if type(self) != type(other):
            if __is_real_number(other):
                return Vector2(self.__x - other, self.__y - other)
            raise Exception("Operations cannot be performed with vectors of other dimensions.")
        return Vector2(self.__x - other.x, self.__y - other.y)
    
    def __mul__(self, other: 'Vector2') -> 'Vector2':
        if type(self) != type(other):
            if __is_real_number(other):
                return Vector2(self.__x * other, self.__y * other)
            raise Exception("Operations cannot be performed with vectors of other dimensions.")
        return Vector2(self.__x * other.x, self.__y * other.y)
    
    def __truediv__(self, other: 'Vector2') -> 'Vector2':
        if type(self) != type(other):
            if __is_real_number(other):
                return Vector2(self.__x / other, self.__y / other)
            raise Exception("Operations cannot be performed with vectors of other dimensions.")
        return Vector2(self.__x / other.x, self.__y / other.y)
    
    def __floordiv__(self, other: 'Vector2') -> 'Vector2':
        if type(self) != type(other):
            if __is_real_number(other):
                return Vector2(self.__x // other, self.__y // other)
            raise Exception("Operations cannot be performed with vectors of other dimensions.")
        return Vector2(self.__x // other.x, self.__y // other.y)

    def __mod__(self, other: 'Vector2') -> 'Vector2':
        if type(self) != type(other):
            if __is_real_number(other):
                return Vector2(self.__x % other, self.__y % other)
            raise Exception("Operations cannot be performed with vectors of other dimensions.")
        return Vector2(self.__x % other.x, self.__y % other.y)        
    
    def __pow__(self, other: int | float) -> float:
        if __is_real_number(other):
            raise Exception("Exponents must be float or int")
        return self.norm() ** other
        
    def __neg__(self) -> 'Vector2':
        return Vector2(-self.__x, -self.__y)

class Vector3:
    def __init__(self, x: float, y: float, z: float) -> None:
        if type(x) != float or type(y) != float or type(z) != float:
            raise Exception("The component of Vector must be a float")

        self.__x = 0.0 if not x else x
        self.__y = 0.0 if not y else y
        self.__z = 0.0 if not z else z

    @property
    def x(self) -> float:
        return self.__x

    @property
    def y(self) -> float:
        return self.__y
    
    @property
    def z(self) -> float:
        return self.__z

    @x.setter
    def x(self, value: float) -> None:
        self.__x = value

    @y.setter
    def y(self, value: float) -> None:
        self.__y = value

    @y.setter
    def z(self, value: float) -> None:
        self.__z = value

    def norm(self) -> float:
        return sqrt(self.__x**2 + self._y**2 +self.__z**2)
    
    def normalize(self) -> 'Vector3':
        __norm = self.norm()
        return Vector3(self.__x/__norm, self.__y/__norm, self.__z/__norm)

    def to_2d(self) -> 'Vector2':
        return Vector2(self.__x, self.__y)
    
    def get_components(self) -> list['Vector3']:
        return [Vector3(self.__x, 0.0, 0.0), Vector3(0.0, self.__y, 0.0), Vector3(0.0, 0.0, self.__z)]
    
    def __add__(self, other: 'Vector3') -> 'Vector3':
        if type(self) != type(other):
            if __is_real_number(other):
                return Vector3(self.__x + other, self.__y + other, self.__z + other)
            raise Exception("Operations cannot be performed with vectors of other dimensions.")
        return Vector3(self.__x + other.x, self.__y + other.y, self.__z + other.__z)
    
    def __sub__(self, other: 'Vector3') -> 'Vector3':
        if type(self) != type(other):
            if __is_real_number(other):
                return Vector3(self.__x - other, self.__y - other, self.__z - other)
            raise Exception("Operations cannot be performed with vectors of other dimensions.")
        return Vector3(self.__x - other.x, self.__y - other.y, self.__z - other.__z)
    
    def __mul__(self, other: 'Vector3') -> 'Vector3':
        if type(self) != type(other):
            if __is_real_number(other):
                return Vector3(self.__x * other, self.__y * other, self.__z * other)
            raise Exception("Operations cannot be performed with vectors of other dimensions.")
        return Vector3(self.__x * other.x, self.__y * other.y, self.__z * other.__z)
    
    def __matmul__(self, other: 'Vector3') -> 'Vector3':
        if type(self) != type(other):
            if __is_real_number(other):
                return Vector3((self.__y * other) - (self.__z * other), (self.__z * other) - (self.__x * other), (self.__x * other) - (self.__y * other))
            raise Exception("Operations cannot be performed with vectors of other dimensions.")
        return Vector3((self.__y * other.z) - (self.__z * other.y), (self.__z * other.x) - (self.__x * other.z), (self.__x * other.y) - (self.__y * other.x))


    def __truediv__(self, other: 'Vector3') -> 'Vector3':
        if type(self) != type(other):
            if __is_real_number(other):
                return Vector3(self.__x / other, self.__y / other, self.__z / other)
            raise Exception("Operations cannot be performed with vectors of other dimensions.")
        return Vector3(self.__x / other.x, self.__y / other.y, self.__z / other.__z)
    
    def __floordiv__(self, other: 'Vector3') -> 'Vector3':
        if type(self) != type(other):
            if __is_real_number(other):
                return Vector3(self.__x // other, self.__y // other, self.__z // other)
            raise Exception("Operations cannot be performed with vectors of other dimensions.")
        return Vector3(self.__x // other.x, self.__y // other.y, self.__z // other.__z)

    def __mod__(self, other: 'Vector3') -> 'Vector3':
        if type(self) != type(other):
            if __is_real_number(other):
                return Vector2(self.__x * other, self.__y * other,self.__z * other)
            raise Exception("Operations cannot be performed with vectors of other dimensions.")
        return Vector3(self.__x % other.x, self.__y % other.y, self.__z % other.__z)
        
    def __pow__(self, other: int | float) -> float:
        if __is_real_number(other):
            raise Exception("Exponents must be float or int")
        return self.norm() ** other
        
    def __neg__(self) -> 'Vector3':
        return Vector3(-self.__x, -self.__y, -self.__z)
