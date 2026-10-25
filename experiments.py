"""기초1 실험 스크립트.

출력 결과로 파이썬의 객체 모델을 직접 확인한다.
실행: python3 experiments.py
"""
import dis
import math
from decimal import Decimal


def section(title):
    """실험 구획을 구분하는 헤더를 출력한다."""
    print(f"\n=== {title} ===")


# ---------------------------------------------------------------
section("1. 변수는 이름표 (같은 객체를 가리키는가?)")
a = 10
b = a
print("a is b      :", a is b)          # True  (같은 객체)
b = b + 1                               # 새 객체 11에 b를 다시 바인딩
print("a, b        :", a, b)            # 10 11
print("a is b      :", a is b)          # False

# ---------------------------------------------------------------
section("2. 가변 객체의 별칭과 복사")
list_a = [1, 2, 3]
list_b = list_a                         # 복사가 아니라 이름표 추가
list_b.append(4)
print("list_a      :", list_a)          # [1, 2, 3, 4]
print("a is b      :", list_a is list_b)  # True

list_c = list_a.copy()                  # 얕은 복사(새 리스트 객체)
list_c.append(5)
print("list_a      :", list_a)          # [1, 2, 3, 4]
print("list_c      :", list_c)          # [1, 2, 3, 4, 5]

# ---------------------------------------------------------------
section("3. 불변 객체 str")
s = "hello"
try:
    s[0] = "H"                          # 불변이라 항목 대입 불가
except TypeError as e:
    print("TypeError   :", e)
print(s.upper(), s)                     # HELLO hello (원본은 그대로)

# ---------------------------------------------------------------
section("4. 숫자: int 정밀도, float 오차, bool")
print("2 ** 100    :", 2 ** 100)        # 1267650600228229401496703205376
print("0.1 + 0.2   :", 0.1 + 0.2)       # 0.30000000000000004
print("== 0.3      :", 0.1 + 0.2 == 0.3)  # False
print("isclose     :", math.isclose(0.1 + 0.2, 0.3))  # True
print("Decimal     :", Decimal("0.1") + Decimal("0.2"))  # 0.3
print("bool is int :", isinstance(True, int), True + True)  # True 2

# ---------------------------------------------------------------
section("5. 연산자: 몫/나머지/연쇄 비교")
print("7 / 2, 7 // 2   :", 7 / 2, 7 // 2)          # 3.5 3
print("-7 // 2, -7 % 3 :", -7 // 2, -7 % 3)        # -4 2
print("1 < 3 < 5       :", 1 < 3 < 5)              # True

# ---------------------------------------------------------------
section("6. 진리값 판정과 단락 평가")
for value in [0, 0.0, "", [], {}, set(), None, "0", [0]]:
    print(f"{value!r:>6} -> {bool(value)}")
print("0 or '기본값'   :", 0 or "기본값")            # 기본값
print("'a' and 'b'     :", "a" and "b")              # b
print("'' and 'b'      :", repr("" and "b"))         # ''

# ---------------------------------------------------------------
section("7. for ... else")
for n in [2, 4, 6]:
    if n % 2:
        print("홀수 발견:", n)
        break
else:
    print("홀수 없음 (break 없이 반복 종료)")         # 이 줄이 출력됨

# ---------------------------------------------------------------
section("8. 함수 인자 종류")


def show(a, b=2, *args, c=3, **kwargs):
    print(f"a={a} b={b} args={args} c={c} kwargs={kwargs}")


show(1)                                 # a=1 b=2 args=() c=3 kwargs={}
show(1, 9, 8, 7, c=0, x=5)              # a=1 b=9 args=(8, 7) c=0 kwargs={'x': 5}

# ---------------------------------------------------------------
section("9. 가변 기본값 함정")


def bad_append(item, bucket=[]):        # 기본값 []는 정의 시점에 한 번만 생성
    bucket.append(item)
    return bucket


def good_append(item, bucket=None):
    if bucket is None:                  # 호출마다 새 리스트 생성
        bucket = []
    bucket.append(item)
    return bucket


print("bad :", bad_append(1), bad_append(2))    # [1, 2] [1, 2]  (같은 리스트 공유)
print("good:", good_append(1), good_append(2))  # [1] [2]

# ---------------------------------------------------------------
section("10. 스코프 LEGB, nonlocal, UnboundLocalError")
x = "global"


def outer():
    x = "enclosing"

    def inner():
        nonlocal x                      # 바로 바깥 함수의 x를 수정
        x = "changed by inner"

    inner()
    return x


print("outer():", outer())              # changed by inner
print("global x:", x)                   # global

counter = 0


def increase():
    counter += 1                        # 대입 -> 지역 변수 취급 -> 값이 없어 오류


try:
    increase()
except UnboundLocalError as e:
    print("UnboundLocalError:", e)      # 메시지 문구는 파이썬 버전마다 다름

# ---------------------------------------------------------------
section("11. 바이트코드 맛보기 (dis)")
dis.dis(lambda p, q: p + q)             # 출력 형식은 버전마다 다름
