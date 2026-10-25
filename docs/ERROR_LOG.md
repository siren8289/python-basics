# 오류 해결 및 예외 학습 로그 (Error & Troubleshooting Log)

## [2026-10-25] 파이썬 언어 특성 관련 주요 오류 분석 및 예방 가이드

### 1. `bool`이 `int`를 상속하여 생기는 유효성 검증 오류
- **발생 상황**: `validate_age(True)` 호출 시
- **오류 증상/문제점**: `isinstance(True, int)`가 `True`를 반환하여 불리언 값이 유효한 나이(1세)로 승인될 위험 존재
- **원인 분석**: 파이썬에서 `bool`은 `int`의 하위 클래스로 구현되어 있음 (`issubclass(bool, int) is True`).
- **해결 방법**: `validator.py`의 `validate_age` 함수 내에서 `isinstance(age, bool)`을 추가로 검사하여 거부 처리함.
  ```python
  if not isinstance(age, int) or isinstance(age, bool):
      return False, "나이는 정수여야 합니다."
  ```
- **재검증 결과**: `test_validator.py`의 `test_bool_is_rejected` 테스트 통과.

---

### 2. 함수 내 `UnboundLocalError` (LEGB 스코프 규칙)
- **발생 상황**: `experiments.py` 섹션 10에서 전역 변수 `counter = 0`에 대해 함수 내에서 `counter += 1` 실행 시
- **오류 로그**:
  ```text
  UnboundLocalError: cannot access local variable 'counter' where it is not associated with a value
  ```
- **원인 분석**: 파이썬 인터프리터는 함수 본문 내에 대입문(`=`, `+=`)이 존재하면 해당 변수를 함수 스코프의 '지역 변수'로 분류함. 따라서 우변의 `counter`를 읽으려 할 때 아직 지역 변수에 값이 할당되지 않아 에러 발생.
- **해결 방법**: 전역 변수를 수정해야 할 경우 `global counter` 키워드를 명시하거나, 객체 상태/반환값을 이용한 함수형 설계를 권장.

---

### 3. 키워드 전용 인자(`*`) 위반 시 `TypeError`
- **발생 상황**: `validate_password("abcdef12", 8, False)` 호출 시
- **오류 로그**:
  ```text
  TypeError: validate_password() takes from 1 to 2 positional arguments but 3 were given
  ```
- **원인 분석**: 함수 시그니처에서 `*` 뒤에 오는 매개변수(`require_digit`, `require_alpha`)는 오직 키워드 형태(`require_digit=False`)로만 전달 가능함.
- **해결 방법**: `validate_password("abcdef12", 8, require_digit=False)` 형태로 명시적 키워드 전달.
- **재검증 결과**: `test_keyword_only_argument`에서 `with self.assertRaises(TypeError):` 검증 완료.
