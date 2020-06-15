#
# 모듈( module )
#   : 변수, 함수, 클래스를 모아놓은 파이썬 스크립트
#   : 모듈( module )은 라이브러리 역활을 하는 파이썬 스크립트로
#     공통적으로 사용할 변수, 함수, 클래스등을 모아놓은 파이썬 스크립트 파일이다.
#
# 패키지( Package ) : 여러 모듈을 설치할 수 있도로 구성한 파일과 디렉터리 집합
#
# 패키지 유형
# 1. 내장 패키지
# 2. third-party( 3자 ) 패키지 / 사용자 패키지
#
# 내장 패키지는 별도의 설치 없이 사용할 수 있으나 third-party 패키지나 사용자
# 패키지는 설치후에 사용할 수 있다.
#
# 설치된 패키지의 모듈을 사용하기 위해서는 'import'문을 사용한다.
#
import mymodule as m
from mymodule import myFunc

myFunc()
m.myPrint( [ 'cat', 'cow', 177, 179, 'tiger'] )













