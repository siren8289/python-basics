# 개발 작업 로그 (Development Log)

## [2026-10-25 20:12] 파이썬 기초 1: 객체 모델 실험 및 입력값 검증기 v2 구축
- **작업 목적**:
  - 파이썬의 핵심 언어 메커니즘(이름표 바인딩, 가변/불변, 진리값 판정, 함수 일급 객체, 스코프)을 11개 실험 코드로 직접 검증
  - 해당 원리를 기반으로 확장된 입력값 검증기(`validator.py`), 실행 데모(`demo.py`), 19개 단위 테스트(`test_validator.py`) 구축
- **변경 및 추가 파일**:
  - `.gitignore`: 파이썬 캐시, 바이트코드, OS 메타데이터 제외 설정
  - `README.md`: 프로젝트 개요 및 실행/테스트 가이드
  - `experiments.py`: 언어 명세 11개 항목 실험 스크립트
  - `validator.py`: 나이, 이메일, 비밀번호 및 전체 검증 함수 구현체
  - `demo.py`: 샘플 입력을 통한 검증기 콘솔 출력 데모
  - `test_validator.py`: unittest 기반 단위 테스트 19개
  - `docs/ARCHITECTURE.md`: 시스템 구조 및 ADR 기록
  - `docs/DEV_LOG.md`: 본 작업 내역
  - `docs/ERROR_LOG.md`: 트러블슈팅 및 예외 케이스 분석
  - `docs/TEST_LOG.md`: 19개 테스트 케이스 검증 결과
- **실행 명령어**:
  1. `python3 experiments.py`
  2. `python3 demo.py`
  3. `python3 -m unittest -v`
- **검증 및 테스트 결과**:
  - `experiments.py`: 11개 섹션 전체 정상 출력 (가변 기본값 함정, float 부동소수점 오차, LEGB 스코프 등 확인)
  - `demo.py`: 4개 샘플 데이터 정상 판정 (성공 1건, 유효성 실패 3건)
  - `test_validator.py`: 19개 단위 테스트 전체 통과 (`Ran 19 tests in 0.001s ... OK`)
- **Commit Hash**: `edb507c` (`feat(python-basics-01): 객체 모델 실험 및 검증기 v2, 테스트 19개 통과`)
