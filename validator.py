"""입력값 검증기 v2.

사용한 개념: 자료형 검사, 조건문, for 반복문, 기본 인자, 키워드 전용 인자,
            함수를 값으로 다루기(일급 객체), 진리값 판정.
모든 검증 함수는 (성공 여부: bool, 메시지: str) 튜플을 반환한다.
"""

OK = "OK"
MISSING_MESSAGE = "필수 항목이 없습니다."


def validate_age(age):
    """나이를 검증한다. 정수이고 0 이상 150 이하일 때 성공."""
    # bool은 int의 하위 타입이라 isinstance(True, int)가 True다. 따로 제외한다.
    if not isinstance(age, int) or isinstance(age, bool):
        return False, "나이는 정수여야 합니다."

    # 연쇄 비교: 0 <= age and age <= 150 과 같다.
    if 0 <= age <= 150:
        return True, OK
    return False, "나이는 0~150 사이여야 합니다."


def validate_email(email):
    """이메일 형식을 간단히 검증한다.

    규칙: 문자열, '@'가 정확히 1개, 로컬 파트가 비어 있지 않음,
          도메인에 '.'이 있고 '.'로 시작하거나 끝나지 않음.
    """
    if not isinstance(email, str):
        return False, "이메일은 문자열이어야 합니다."

    email = email.strip()               # str은 불변 -> 새 문자열을 같은 이름에 다시 바인딩

    if email.count("@") != 1:
        return False, "'@'는 정확히 하나여야 합니다."

    local, domain = email.split("@")    # 언패킹: 길이 2인 리스트를 두 이름에 대입
    if not local:                       # 빈 문자열은 거짓
        return False, "'@' 앞 부분이 비어 있습니다."

    if "." not in domain or domain.startswith(".") or domain.endswith("."):
        return False, "도메인 형식이 잘못되었습니다."
    return True, OK


def validate_password(password, min_length=8, *, require_digit=True, require_alpha=True):
    """비밀번호를 검증한다.

    min_length는 기본 인자, require_*는 '*' 뒤에 있어 키워드로만 전달할 수 있다.
    예) validate_password("abcdef12", 12)  /  validate_password("abcdefgh", require_digit=False)
    """
    if not isinstance(password, str):
        return False, "비밀번호는 문자열이어야 합니다."

    if len(password) < min_length:
        return False, f"비밀번호는 최소 {min_length}자 이상이어야 합니다."

    has_digit = False
    has_alpha = False
    for ch in password:
        if ch.isdigit():
            has_digit = True
        elif ch.isalpha():
            has_alpha = True
        if has_digit and has_alpha:
            break                       # 둘 다 찾았으면 더 볼 필요 없음

    if require_digit and not has_digit:
        return False, "숫자를 최소 1개 포함해야 합니다."
    if require_alpha and not has_alpha:
        return False, "문자를 최소 1개 포함해야 합니다."
    return True, OK


# 함수도 객체이므로 딕셔너리 값으로 저장할 수 있다. (필드명 -> 검증 함수)
VALIDATORS = {
    "age": validate_age,
    "email": validate_email,
    "password": validate_password,
}


def validate_all(data):
    """딕셔너리 입력 전체를 검증한다.

    반환: (전체 성공 여부, {필드명: 오류 메시지}).
    """
    errors = {}
    for field, func in VALIDATORS.items():
        if field not in data:
            errors[field] = MISSING_MESSAGE
            continue                    # 다음 필드로
        ok, message = func(data[field])  # func는 validate_xxx 중 하나
        if not ok:
            errors[field] = message
    # errors가 비어 있으면(거짓) 성공. not errors는 bool을 반환한다.
    return (not errors), errors
