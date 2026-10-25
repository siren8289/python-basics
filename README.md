# python-basics-01: 파이썬 기초 1 (변수·자료형·제어문·함수)

파이썬의 객체 모델(이름표 바인딩, 가변/불변, 진리값 판정, 스코프)을 실험으로 확인하고, 이를 활용한 실무형 입력값 검증기(`validator.py`)를 구현 및 테스트합니다.

## 파일 구성

```
.
├── experiments.py      # 객체 모델, 진리값, 가변 기본값, 스코프 등 11개 개념 검증 실험
├── validator.py        # 입력값 검증기 v2 (나이, 이메일, 비밀번호 및 전체 검증)
├── demo.py             # validator.py 샘플 데이터 실행 및 출력 데모
├── test_validator.py   # unittest 기반 단위 테스트 19개
├── docs/               # 작업 로그 및 아키텍처 문서
│   ├── ARCHITECTURE.md # 아키텍처 및 설계 문서
│   ├── DEV_LOG.md      # 개발 작업 로그
│   ├── ERROR_LOG.md    # 오류 해결 로그
│   ├── TEST_LOG.md     # 테스트 검증 로그
│   └── error-logs/     # 개별 상세 오류 트러블슈팅 로그
└── README.md
```

## 실행 및 테스트 가이드 (macOS 기준)

### 1. 객체 모델 실험 실행
```zsh
python3 experiments.py
```

### 2. 검증기 데모 실행
```zsh
python3 demo.py
```

### 3. 단위 테스트 실행 (19개 테스트)
```zsh
python3 -m unittest -v
```
