# Python 기초 학습 정리 보고서

이 문서는 **"04_Python 기초"** 강의 자료를 학습한 뒤,  
실습을 통해 작성한 Python 예제 파일들과 그 과정에서 배운 내용을 정리한 보고서입니다.  

---

## 1️⃣ 강의에서 배운 주요 내용

강의 자료(`04_Python 기초.pptx`)를 통해 다음과 같은 내용을 학습했습니다:

- **Python 및 VS Code 설치**
  - python.org에서 최신 버전 다운로드 및 설치
  - VS Code 설치 및 Python Extension Pack, Jupyter 확장팩 활용
  - `python --version`, `py -0` 등을 이용한 버전 확인 방법

- **VS Code 기본 기능**
  - 터미널 사용법 (Ctrl + `)
  - 명령 팔레트 (Ctrl + Shift + P)
  - 주요 단축키 (코드 실행, 디버깅, 주석 처리 등)

- **Python 가상환경 관리**
  - `python -m venv .venv` 로 가상환경 생성
  - Windows: `.\.venv\Scripts\Activate` / Linux: `source .venv/bin/activate`
  - `requirements.txt` 파일을 통한 환경 공유 방법

- **Python 실행 방법**
  - `.py` 파일 직접 실행: `python main.py`
  - Notebook 실행: `jupyter notebook main.ipynb`
  - 디버깅 및 코드 블록 단위 실행 방법

- **실습 주제**
  - 다양한 `print()` 함수 사용법
  - `rich` 모듈을 활용한 고급 출력
  - requirements.txt 작성 및 관리

---

## 2️⃣ 실습 파일 소개

강의 내용을 바탕으로 다음 4개의 실습 파일을 작성했습니다:

### 📄 main_print_v1 3.py
- Python 기본 `print()` 함수 실습
- f-string, format(), % 포맷팅 방식 비교
- `sep`, `end` 옵션 활용
- 여러 줄 출력 및 딕셔너리 출력

### 📄 main_print_v2.py
- `rich` 라이브러리를 활용한 출력 실습
- 컬러풀한 문자열 출력
- Panel(패널), Table(테이블) 활용
- `rich.print`에서 `sep`, `end` 옵션도 사용 가능함을 확인

### 📄 main_print_v1.ipynb
- `main_print_v1 3.py` 내용을 Jupyter Notebook으로 옮겨 셀 단위 실행
- print 함수 결과를 단계별로 확인하며 학습 가능

### 📄 requirements.txt
- 프로젝트 실행에 필요한 라이브러리 정리
- `rich`, `Pygments`, `markdown-it-py` 등이 포함됨
- `pip freeze > requirements.txt` 명령어를 통해 생성

---

## 3️⃣ 배운 점 및 느낀 점

- `print()` 함수는 단순한 출력 이상의 다양한 활용법이 있다는 것을 알게 되었습니다.
- f-string은 직관적이고 가독성이 높아서 실무에서 가장 많이 쓰일 것 같다고 느꼈습니다.
- `rich` 모듈을 사용하면 콘솔 출력만으로도 가독성이 좋아지고, 학습용/시각화용으로 유용하다는 점을 배웠습니다.
- VS Code 환경에서 가상환경을 만들어 프로젝트를 관리하는 방법을 익혀, 앞으로 다른 프로젝트에도 적용할 수 있을 것 같습니다.
- Jupyter Notebook을 이용하면 코드와 결과를 동시에 관리할 수 있어서 학습과 공유에 적합하다는 걸 알게 되었습니다.

---

## 4️⃣ 실행 방법 (정리)

1. 가상환경 생성
   ```bash
   python -m venv .venv
2. 가상환경 활성화

Windows
.\.venv\Scripts\Activate

3. 가상황경 비활성화
deactivate

4. 가상환경 삭제
rmdir /s .venv