from math import sqrt

def _is_real_num(num):
        if isinstance(num, float) or isinstance(num, int):
            return True
        else:
            return False

class Vector2:
    def __init__(self, x: float | int | None, y: float | int | None) -> None:
        if not _is_real_num(x) or not _is_real_num(y):
            raise Exception("The component of Vector must be a float, int or None")

        self.__x = 0.0 if not x else float(x)
        self.__y = 0.0 if not y else float(y)

    @property
    def x(self) -> float:
        return self.__x

    @property
    def y(self) -> float:
        return self.__y
    
    @x.setter
    def x(self, value: float | int) -> None:
        self.__x = float(value)

    @y.setter
    def y(self, value: float | int) -> None:
        self.__y = float(value)
    
    def norm(self) -> float:
        return sqrt(self.__x**2 + self.__y**2)
    
    def normalize(self) -> 'Vector2':
        __norm = self.norm
        return Vector2(self.__x/__norm, self.__y/__norm)
    
    def to_3d(self) -> 'Vector3':
        return Vector3(self.__x, self.__y, 0.0)

    def get_components(self) -> list['Vector2']:
        return [Vector2(self.__x, 0.0), Vector2(0.0, self.__y)]

    def __add__(self, other: 'Vector2' | int | float) -> 'Vector2':
        if type(self) != type(other):
            if _is_real_num(other):
                return self + Vector2(other, other)
            raise Exception("Operations cannot be performed with vectors of other dimensions.")
        return Vector2(self.__x + other.x, self.__y + other.y)
    
    def __sub__(self, other: 'Vector2' | int | float) -> 'Vector2':
        if type(self) != type(other):
            if _is_real_num(other):
                return self - Vector2(other, other)
            raise Exception("Operations cannot be performed with vectors of other dimensions.")
        return Vector2(self.__x - other.x, self.__y - other.y)
    
    def __mul__(self, other: 'Vector2' | int | float) -> 'Vector2':
        if type(self) != type(other):
            if _is_real_num(other):
                return self * Vector2(other, other)
            raise Exception("Operations cannot be performed with vectors of other dimensions.")
        return Vector2(self.__x * other.x, self.__y * other.y)
    
    def __truediv__(self, other: 'Vector2' | int | float) -> 'Vector2':
        if type(self) != type(other):
            if _is_real_num(other):
                return self / Vector2(other, other)
            raise Exception("Operations cannot be performed with vectors of other dimensions.")
        return Vector2(self.__x / other.x, self.__y / other.y)
    
    def __floordiv__(self, other: 'Vector2' | int | float) -> 'Vector2':
        if type(self) != type(other):
            if _is_real_num(other):
                return self // Vector2(other, other)
            raise Exception("Operations cannot be performed with vectors of other dimensions.")
        return Vector2(self.__x // other.x, self.__y // other.y)

    def __mod__(self, other: 'Vector2' | int | float) -> 'Vector2':
        if type(self) != type(other):
            if _is_real_num(other):
                return self % Vector2(other, other)
            raise Exception("Operations cannot be performed with vectors of other dimensions.")
        return Vector2(self.__x % other.x, self.__y % other.y)        
    
    def __pow__(self, other: int | float) -> float:
        if _is_real_num(other):
            raise Exception("Exponents must be float or int")
        return self.norm() ** other
        
    def __neg__(self) -> 'Vector2':
        return Vector2(-self.__x, -self.__y)

class Vector3:
    def __init__(self, x: float | int | None, y: float | int | None, z: float | int | None) -> None:
        if not _is_real_num(x) or not _is_real_num(y) or not _is_real_num(z):
            raise Exception("The component of Vector must be a float, int or None")

        self.__x = 0.0 if not x else float(x)
        self.__y = 0.0 if not y else float(y)
        self.__z = 0.0 if not z else float(z)

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
        self.__x = float(value)

    @y.setter
    def y(self, value: float) -> None:
        self.__y = float(value)

    @y.setter
    def z(self, value: float) -> None:
        self.__z = float(value)

    def norm(self) -> float:
        return sqrt(self.__x**2 + self._y**2 +self.__z**2)
    
    def normalize(self) -> 'Vector3':
        __norm = self.norm()
        return Vector3(self.__x/__norm, self.__y/__norm, self.__z/__norm)

    def to_2d(self) -> 'Vector2':
        return Vector2(self.__x, self.__y)
    
    def get_components(self) -> list['Vector3']:
        return [Vector3(self.__x, 0.0, 0.0), Vector3(0.0, self.__y, 0.0), Vector3(0.0, 0.0, self.__z)]
    
    def __add__(self, other: 'Vector3' | int | float) -> 'Vector3':
        if type(self) != type(other):
            if _is_real_num(other):
                return self + Vector3(other, other, other)
            raise Exception("Operations cannot be performed with vectors of other dimensions.")
        return Vector3(self.__x + other.x, self.__y + other.y, self.__z + other.__z)
    
    def __sub__(self, other: 'Vector3' | int | float) -> 'Vector3':
        if type(self) != type(other):
            if _is_real_num(other):
                return self - Vector3(other, other, other)
            raise Exception("Operations cannot be performed with vectors of other dimensions.")
        return Vector3(self.__x - other.x, self.__y - other.y, self.__z - other.__z)
    
    def __mul__(self, other: 'Vector3' | int | float) -> 'Vector3':
        if type(self) != type(other):
            if _is_real_num(other):
                return self * Vector3(other, other, other)
            raise Exception("Operations cannot be performed with vectors of other dimensions.")
        return Vector3(self.__x * other.x, self.__y * other.y, self.__z * other.__z)
    
    def __matmul__(self, other: 'Vector3' | int | float) -> 'Vector3':
        if type(self) != type(other):
            if _is_real_num(other):
                return self @ Vector3(other, other, other)
            raise Exception("Operations cannot be performed with vectors of other dimensions.")
        return Vector3((self.__y * other.z) - (self.__z * other.y), (self.__z * other.x) - (self.__x * other.z), (self.__x * other.y) - (self.__y * other.x))


    def __truediv__(self, other: 'Vector3' | int | float) -> 'Vector3':
        if type(self) != type(other):
            if _is_real_num(other):
                return self / Vector3(other, other, other)
            raise Exception("Operations cannot be performed with vectors of other dimensions.")
        return Vector3(self.__x / other.x, self.__y / other.y, self.__z / other.__z)
    
    def __floordiv__(self, other: 'Vector3' | int | float) -> 'Vector3':
        if type(self) != type(other):
            if _is_real_num(other):
                return self // Vector3(other, other, other)
            raise Exception("Operations cannot be performed with vectors of other dimensions.")
        return Vector3(self.__x // other.x, self.__y // other.y, self.__z // other.__z)

    def __mod__(self, other: 'Vector3' | int | float) -> 'Vector3':
        if type(self) != type(other):
            if _is_real_num(other):
                return self % Vector3(other, other, other)
            raise Exception("Operations cannot be performed with vectors of other dimensions.")
        return Vector3(self.__x % other.x, self.__y % other.y, self.__z % other.__z)
        
    def __pow__(self, other: int | float) -> float:
        if _is_real_num(other):
            raise Exception("Exponents must be float or int")
        return self.norm() ** other
        
    def __neg__(self) -> 'Vector3':
        return Vector3(-self.__x, -self.__y, -self.__z)