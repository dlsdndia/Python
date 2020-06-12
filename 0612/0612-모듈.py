#
# 모듈( module )
#  : 변수, 함수, 클래스를 모아놓은 파이썬 스크립트
#  : 모듈( module )은 라이브러리 역할을 하는 파이썬 스크립트로 공통적ㄷ으로 사용할 변수, 함수, 클래스등을 모아놓은 파이썬 스크립트 파일이다.
#
# 패키지( package ) : 여러 모듈을 설치할 수 있도록 구성한 파일과 디렉터리 집합
#
# 패키지 유형
# 1. 내장 패키지
# 2. third-party(3자) 패키지, 사용자 패키지
#
# 내장 패키지는 별도의 설치 없이 사용할 수 있으나 third-party패키지나 사용자 패키지는 설치후에 사용할 수있다.
#
# 설치된 패키지의 모듈을 사용하기 위해서는 'import'문을 사용한다.
#
import mymodule

mymodule.myFunc()# --> 가지고 오고픈 모듈이 있는 스크립파일 이름을  위에 imort mymodule하고 여기처럼 한다 mymodule파일 확인하기
#                      프로젝트에서 만든 것은 프로젝트 안에서만 사용가능
from mymodule import myFunc # 이렇게 하면 해당 함수를 모듈로 불러올 때 모듈이름.myFunc를 안해도 그냥 myFunc()만 해도 됨

import mymodule
import mymodule as m # ->이렇게 하면 m만하면 mymodule같이 풀이름을 안 써도 됨

# if __name__== '__main__' --> 이 밑에있는것만 단독으로 모듈로 불러올 때

#
# mymodule
#
def myFunc():
    print( 'My Function -> my Function()' )

def myPrint( values ):
    colum_count = 1
    for value in values:
        print( '{}\t'.format( value ), end = '' )
        colum_count += 1
        if colum_count > 10:
            print()
            colum_count = 1

#if __name__== '_main__':
    myFunc()
    myPrint( [ 1, 2, 'apple', 'banana', 10.5, 3, 4, 5, 6, 7, 8, 9, 10 ] )
















