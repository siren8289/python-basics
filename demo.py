"""validator.py를 직접 호출해 결과를 눈으로 확인한다. 실행: python3 demo.py"""
from validator import validate_all

samples = [
    {"age": 30, "email": "siren@example.com", "password": "abcdef12"},
    {"age": -1, "email": "nope", "password": "short"},
    {"age": True, "email": "a@.com", "password": "12345678"},
    {"age": 20, "email": "a@b.com"},        # password 누락
]

for idx, sample in enumerate(samples, start=1):
    ok, errors = validate_all(sample)
    print(f"[{idx}] ok={ok}")
    for field, message in errors.items():
        print(f"     - {field}: {message}")
