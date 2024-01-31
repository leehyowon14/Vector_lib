"""2차원, 3차원 벡터를 표현하고 연산하기 위한 모듈
"""

from __future__ import annotations
from math import sqrt
from typing import Any

def _is_real_num(arg: Any) -> bool:
    """주어진 인자가 실수인지 확인.

    Args:
        arg (Any): 실수인지 확인할 인자.

    Returns:
        bool: 실수일 시 True를, 문자열 등의 자료형일시 False를 리턴.
    """
    return isinstance(arg, (float, int))

class Vector2:
    """2차원 벡터를 표현하기 위한 클래스
    """
    def __init__(self, x: float | int | None = 0.0, y: float | int | None = 0.0) -> None:
        """2차원 평면벡터를 정의함.

        Args:
            x (float | int | None, optional): 평면벡터의 X축 성분. float 자료형으로 저장됨. Defaults to 0.0.
            y (float | int | None, optional): 평면벡터의 Y축 성분. float 자료형으로 저장됨. Defaults to 0.0.

        Raises:
            TypeError: 정수, 실수, 혹은 None이 아닌 다른 타입의 값이 인자로 주어졌을 때 발생하는 에러.
        """
        if not _is_real_num(x) or not _is_real_num(y):
            raise TypeError("The component of Vector must be a float, int or None")

        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self) -> float:
        """해당 평면벡터의 X축 성분을 스칼라 값으로 불러옴.

        Returns:
            float: X축 성분.
        """
        return self.__x

    @property
    def y(self) -> float:
        """해당 평면벡터의 Y축 성분을 스칼라 값으로 불러옴.

        Returns:
            float: Y축 성분.
        """
        return self.__y

    @x.setter
    def x(self, value: float | int) -> None:
        """해당 평면벡터의 X축 성분을 설정함.

        Args:
            value (float | int): 설정할 X축 성분, float 자료형으로 저장됨.
        """
        self.__x = float(value)

    @y.setter
    def y(self, value: float | int) -> None:
        """해당 평면벡터의 Y축 성분을 설정함.

        Args:
            value (float | int): 설정할 Y축 성분, float 자료형으로 저장됨.
        """
        self.__y = float(value)

    def norm(self) -> float:
        """해당 평면벡터의 크기를 구함.

        Returns:
            float: 벡터의 크기.
        """
        return sqrt(self.__x**2 + self.__y**2)

    def normalize(self) -> None:
        """해당 평면벡터를 단위 벡터로 변환함.

        Returns:
            Vector2: 단위벡터로 변환된 평면벡터.
        """
        __norm = self.norm()
        self.__x = self.__x/__norm
        self.__y = self.__y/__norm

    def to_3d(self) -> Vector3:
        """해당 평면벡터를 공간벡터로 변환함. Z축 성분은 0.0으로 설정됨.

        Returns:
            Vector3: 공간벡터로 변환된 평면벡터.
        """
        return Vector3(self.__x, self.__y, 0.0)

    def get_components(self) -> list[Vector2]:
        """해당 평면벡터를 각각의 성분으로 나눈 후 리스트로 반환함.

        Returns:
            list[Vector2]: 각 축의 성분 벡터를 리스트[X, Y]의 형태로 반환함.
        """
        return [Vector2(self.__x, 0.0), Vector2(0.0, self.__y)]

    def __add__(self, other: Vector2 | int | float) -> Vector2:
        """평면벡터의 합을 계산함.

        Args:
            other (Vector2 | int | float): 해당 평면벡터에 더해질 평면벡터.

        Raises:
            TypeError: 타 차원의 벡터와 연산하는 경우 빌생하는 에러.

        Returns:
            Vector2: 연산 결과.
        """
        if not isinstance(other, Vector2):
            if _is_real_num(other):
                return self + Vector2(other, other)
            raise TypeError("Operations cannot be performed with vectors of other dimensions.")
        return Vector2(self.__x + other.x, self.__y + other.y)

    def __sub__(self, other: Vector2 | int | float) -> Vector2:
        """평면벡터의 차를 계산함.

        Args:
            other (Vector2 | int | float): 해당 평면벡터에서 빠질 평면벡터.

        Raises:
            TypeError: 타 차원의 벡터와 연산하는 경우 발생하는 에러.

        Returns:
            Vector2: 연산 결과.
        """
        if not isinstance(other, Vector2):
            if _is_real_num(other):
                return self - Vector2(other, other)
            raise TypeError("Operations cannot be performed with vectors of other dimensions.")
        return Vector2(self.__x - other.x, self.__y - other.y)

    def __mul__(self, other: Vector2 | int | float) -> Vector2:
        """평면벡터의 내적을 계산함.

        Args:
            other (Vector2 | int | float): 해당 평면벡터와 내적할 평면벡터.

        Raises:
            TypeError: 타 차원의 벡터와 연산하는 경우 발생하는 에러.

        Returns:
            float: 연산 결과. (스칼라)
        """
        if not isinstance(other, Vector2):
            if _is_real_num(other):
                return self * Vector2(other, other)
            raise TypeError("Operations cannot be performed with vectors of other dimensions.")
        return self.__x * other.x + self.__y * other.y

    def __truediv__(self, other: Vector2 | int | float) -> Vector2:
        """평면벡터의 나눗셈을 계산함.

        Args:
            other (Vector2 | int | float): 평면벡터의 나눗셈에서의 제수.

        Raises:
            TypeError: 타 차원의 벡터와 연산하는 경우 발생하는 에러.

        Returns:
            Vector2: 연산 결과.
        """
        if not isinstance(other, Vector2):
            if _is_real_num(other):
                return self / Vector2(other, other)
            raise TypeError("Operations cannot be performed with vectors of other dimensions.")
        return Vector2(self.__x / other.x, self.__y / other.y)

    def __floordiv__(self, other: Vector2 | int | float) -> Vector2:
        """평면벡터의 나눗셈. 소수점이 아닌, 몫을 계산.

        Args:
            other (Vector2 | int | float): 평면벡터의 나눗셈에서의 제수.

        Raises:
            TypeError: 타 차원의 벡터와 연산하는 경우 발생하는 에러.

        Returns:
            Vector2: 연산 결과
        """
        if not isinstance(other, Vector2):
            if _is_real_num(other):
                return self // Vector2(other, other)
            raise TypeError("Operations cannot be performed with vectors of other dimensions.")
        return Vector2(self.__x // other.x, self.__y // other.y)

    def __mod__(self, other: Vector2 | int | float) -> Vector2:
        """평면벡터의 나눗셈. 소수점이 아닌, 나머지를 게산.

        Args:
            other (Vector2 | int | float): 평면벡터의 나눗셈에서의 제수.

        Raises:
            TypeError: 타 차원의 벡터와 연산하는 경우 발생하는 에러.

        Returns:
            Vector2: 연산 결과.
        """
        if not isinstance(other, Vector2):
            if _is_real_num(other):
                return self % Vector2(other, other)
            raise TypeError("Operations cannot be performed with vectors of other dimensions.")
        return Vector2(self.__x % other.x, self.__y % other.y)

    def __pow__(self, other: int | float) -> float:
        """평면벡터의 X제곱을 계산.

        Args:
            other (int | float): 지수.

        Raises:
            TypeError: 타 차원의 벡터와 연산하는 경우 발생하는 에러.

        Returns:
            float: 연신 결과. (스칼라)
        """
        if _is_real_num(other):
            raise TypeError("Exponents must be float or int")
        return self.norm() ** other

    def __neg__(self) -> Vector2:
        """해당 평면벡터의 역벡터를 구함.

        Returns:
            Vector2: 해당 평면벡터의 역벡터.
        """
        return Vector2(-self.__x, -self.__y)

    def __eq__(self, other: Vector2) -> bool:
        """두 평면벡터가 같은지 비교함.

        Args:
            other (Vector2): 비교할 평면벡터.

        Raises:
            TypeError: 평면벡터가 아닌 자료형과 비교하는 경우 발생하는 에러.

        Returns:
            bool: 두 벡터가 같을 시 True를 반환함. 반대의 경우 False를 반환함.
        """
        if not isinstance(other, Vector2):
            raise TypeError("Operations cannot be performed with vectors of other dimensions.")
        return self.__x == other.x and self.__y == other.y

    def __ne__(self, other: Vector2) -> bool:
        """두 평면벡터가 다른지를 비교함.

        Args:
            other (Vector2): 비교할 평면벡터.

        Returns:
            bool: 두 벡터가 다를 시 True를 반환함. 반대의 경우 False를 반환함.
        """
        return not self == other

class Vector3:
    """3차원 벡터를 표현하기 위한 클래스
    """
    def __init__(
            self, x: float | int | None = 0.0,
            y: float | int | None = 0.0,
            z: float | int | None = 0.0
        ) -> None:

        """3차원 공간벡터를 정의함.

        Args:
            x (float | int | None, optional): 공간벡터의 X축 성분. float 자료형으로 저장됨. Defaults to 0.0.
            y (float | int | None, optional): 공간벡터의 Y축 성분. float 자료형으로 저장됨. Defaults to 0.0.
            z (float | int | None, optional): 공간벡터의 Z축 성분. float 자료형으로 저장됨. Defaults to 0.0.

        Raises:
            TypeError: 정수, 실수, 혹은 None이 아닌 다른 타입의 값이 인자로 주어졌을 때 발생하는 에러.
        """
        if not _is_real_num(x) or not _is_real_num(y) or not _is_real_num(z):
            raise TypeError("The component of Vector must be a float, int or None")

        self.__x = float(x)
        self.__y = float(y)
        self.__z = float(z)

    @property
    def x(self) -> float:
        """해당 공간벡터의 X축 성분을 스칼라 값으로 불러옴

        Returns:
            float: X축 성분
        """
        return self.__x

    @property
    def y(self) -> float:
        """해당 공간벡터의 Y축 성분을 스칼라 값으로 불러옴

        Returns:
            float: Y축 성분
        """
        return self.__y

    @property
    def z(self) -> float:
        """해당 공간벡터의 Z축 성분을 스칼라 값으로 불러옴

        Returns:
            float: Z축 성분
        """
        return self.__z

    @x.setter
    def x(self, value: float | int) -> None:
        """해당 공간벡터의 X축 성분을 설정함

        Args:
            value (float | int): 설정할 X축 성분, float 자료형으로 저장됨.
        """
        self.__x = float(value)

    @y.setter
    def y(self, value: float | int) -> None:
        """해당 공간벡터의 Y축 성분을 설정함

        Args:
            value (float | int): 설정할 Y축 성분, float 자료형으로 저장됨.
        """
        self.__y = float(value)

    @z.setter
    def z(self, value: float | int) -> None:
        """해당 공간벡터의 Z축 성분을 설정함

        Args:
            value (float | int): 설정할 Z축 성분, float 자료형으로 저장됨.
        """
        self.__z = float(value)

    def norm(self) -> float:
        """해당 공간벡터의 크기를 구함.

        Returns:
            float: 벡터의 크기.
        """
        return sqrt(self.__x**2 + self.__y**2 +self.__z**2)

    def normalize(self) -> None:
        """해당 공간벡터를 단위 벡터로 변환함.

        Returns:
            Vector2: 단위벡터로 변환된 공간벡터.
        """
        __norm = self.norm()
        self.__x = self.__x/__norm
        self.__y = self.__y/__norm
        self.__z = self.__z/__norm

    def to_2d(self) -> Vector2:
        """해당 공간벡터를 평면벡터로 변환함. Z축 성분은 소실됨.

        Returns:
            Vector2: 평면벡터로 변환된 공간벡터.
        """
        return Vector2(self.__x, self.__y)

    def get_components(self) -> list[Vector3]:
        """해당 공간벡터를 각각의 성분으로 나눈 후 리스트로 반환함.

        Returns:
            list[Vector3]: 각 축의 성분 벡터를 리스트[X, Y, Z]의 형태로 반환함.
        """
        return [
            Vector3(self.__x, 0.0, 0.0),
            Vector3(0.0, self.__y, 0.0),
            Vector3(0.0, 0.0, self.__z)
        ]

    def __add__(self, other: Vector3 | int | float) -> Vector3:
        """공간벡터의 합을 계산함.

        Args:
            other (Vector3 | int | float): 해당 공간벡터에 더해질 공간벡터.

        Raises:
            TypeError: 타 차원의 벡터와 연산하는 경우 빌생하는 에러.

        Returns:
            Vector3: 연산 결과.
        """
        if not isinstance(other, Vector3):
            if _is_real_num(other):
                return self + Vector3(other, other, other)
            raise TypeError("Operations cannot be performed with vectors of other dimensions.")
        return Vector3(self.__x + other.x, self.__y + other.y, self.__z + other.z)

    def __sub__(self, other: Vector3 | int | float) -> Vector3:
        """공간벡터의 차를 계산함.

        Args:
            other (Vector3 | int | float): 해당 공간벡터에서 빠질 공간벡터.

        Raises:
            TypeError: 타 차원의 벡터와 연산하는 경우 발생하는 에러.

        Returns:
            Vector3: 연산 결과.
        """
        if not isinstance(other, Vector3):
            if _is_real_num(other):
                return self - Vector3(other, other, other)
            raise TypeError("Operations cannot be performed with vectors of other dimensions.")
        return Vector3(self.__x - other.x, self.__y - other.y, self.__z - other.z)

    def __mul__(self, other: Vector3 | int | float) -> Vector3:
        """공간벡터의 내적을 계산함.

        Args:
            other (Vector3 | int | float): 해당 공간벡터와 내적할 공간벡터.

        Raises:
            TypeError: 타 차원의 벡터와 연산하는 경우 발생하는 에러.

        Returns:
            float: 연산 결과. (스칼라)
        """
        if not isinstance(other, Vector3):
            if _is_real_num(other):
                return self * Vector3(other, other, other)
            raise TypeError("Operations cannot be performed with vectors of other dimensions.")
        return self.__x * other.x + self.__y * other.y + self.__z * other.z

    def __matmul__(self, other: Vector3 | int | float) -> Vector3:
        """공간벡터의 외적을 계산함

        Args:
            other (Vector3 | int | float): 해당 공간벡터와 외적할 공간벡터

        Raises:
            TypeError: 타 차원의 벡터와 연산하는 경우 발생하는 에러.

        Returns:
            Vector3: 연산 결과.
        """
        if not isinstance(other, Vector3):
            if _is_real_num(other):
                return self @ Vector3(other, other, other)
            raise TypeError("Operations cannot be performed with vectors of other dimensions.")
        return Vector3(
            (self.__y * other.z) - (self.__z * other.y),
            (self.__z * other.x) - (self.__x * other.z),
            (self.__x * other.y) - (self.__y * other.x)
        )


    def __truediv__(self, other: Vector3 | int | float) -> Vector3:
        """공간벡터의 나눗셈을 계산함.

        Args:
            other (Vector3 | int | float): 공간벡터의 나눗셈에서의 제수.

        Raises:
            TypeError: 타 차원의 벡터와 연산하는 경우 발생하는 에러.

        Returns:
            Vector3: 연산 결과.
        """
        if not isinstance(other, Vector3):
            if _is_real_num(other):
                return self / Vector3(other, other, other)
            raise TypeError("Operations cannot be performed with vectors of other dimensions.")
        return Vector3(self.__x / other.x, self.__y / other.y, self.__z / other.z)

    def __floordiv__(self, other: Vector3 | int | float) -> Vector3:
        """공간벡터의 나눗셈. 소수점이 아닌, 몫을 계산.

        Args:
            other (Vector3 | int | float): 공간벡터의 나눗셈에서의 제수.

        Raises:
            TypeError: 타 차원의 벡터와 연산하는 경우 발생하는 에러.

        Returns:
            Vector3: 연산 결과
        """
        if not isinstance(other, Vector3):
            if _is_real_num(other):
                return self // Vector3(other, other, other)
            raise TypeError("Operations cannot be performed with vectors of other dimensions.")
        return Vector3(self.__x // other.x, self.__y // other.y, self.__z // other.z)

    def __mod__(self, other: Vector3 | int | float) -> Vector3:
        """공간벡터의 나눗셈. 소수점이 아닌, 나머지를 게산.

        Args:
            other (Vector3 | int | float): 공간벡터의 나눗셈에서의 제수.

        Raises:
            TypeError: 타 차원의 벡터와 연산하는 경우 발생하는 에러.

        Returns:
            Vector3: 연산 결과.
        """
        if not isinstance(other, Vector3):
            if _is_real_num(other):
                return self % Vector3(other, other, other)
            raise TypeError("Operations cannot be performed with vectors of other dimensions.")
        return Vector3(self.__x % other.x, self.__y % other.y, self.__z % other.z)

    def __pow__(self, other: int | float) -> float:
        """공간벡터의 X제곱을 계산.

        Args:
            other (int | float): 지수.

        Raises:
            TypeError: 타 차원의 벡터와 연산하는 경우 발생하는 에러.

        Returns:
            float: 연신 결과. (스칼라)
        """
        if _is_real_num(other):
            raise TypeError("Exponents must be float or int")
        return self.norm() ** other

    def __neg__(self) -> Vector3:
        """해당 공간벡터의 역벡터를 구함.

        Returns:
            Vector3: 해당 공간벡터의 역벡터.
        """
        return Vector3(-self.__x, -self.__y, -self.__z)

    def __eq__(self, other: Vector3) -> bool:
        """두 공간벡터가 같은지 비교함

        Args:
            other (Vector3): 비교할 공간벡터.

        Raises:
            TypeError: 공간벡터가 아닌 자료형과 비교하는 경우 발생하는 에러.

        Returns:
            bool: 두 벡터가 같을 시 True를 반환함. 반대의 경우 False를 반환함.
        """
        if not isinstance(other, Vector3):
            raise TypeError("Operations cannot be performed with vectors of other dimensions.")
        return self.__x == other.x and self.__y == other.y and self.__z == other.z

    def __ne__(self, other: Vector3) -> bool:
        """두 공간벡터가 다른지를 비교함.

        Args:
            other (Vector3): 비교할 공간벡터.

        Returns:
            bool: 두 벡터가 다를 시 True를 반환함. 반대의 경우 False를 반환함.
        """
        return not self == other
