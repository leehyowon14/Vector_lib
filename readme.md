# Vector library
##### by. leehyowon14

2차원, 3차원 벡터를 파이썬에서 손쉽게 사용할 수 있게 해주는 라이브러리입니다.

Python 3.10 +
## Usage
### 2D Vector
- 선언
    ```py
    Vector2(x, y)
    ```
    인자 x, y의 타입은 float여야 합니다.
- 덧셈
    ```py
    Vector2(x1, y1) + Vector2(x2, y2)
    ```
    Output: `Vector2(x1+x2, y1+y2)`
    

to-do :
- Vector2
    - [x] rotate(degree) 함수
    - [ ] 비교연산자
    - [ ] 두 각 사이 각도 구하기

- Vector3
    - [x] rotate(Vector3 rotate) 함수 (linear transformation 실행)
    - [ ] 비교연산자