from flask import Flask

app = Flask(__name__)

print(app)

"""
초기 환경설정
: python은 컴파일 언어가 아닌 인터프리터 언어라 초기 환경세팅이 굉장히 중요함
 - Formatter : 언어가 비교적 유연하기 때문에 협업시 코딩 컨벤션을 맞추기 위함.
 - Linter : 인터프리터 언어라 호출되지 않은 함수는 오류가 있어도 디버깅 시 알 수 없음. 이를 잡아낼 수 있게 하기 위한 툴.
"""
