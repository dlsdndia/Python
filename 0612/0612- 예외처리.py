#
# 예외 처리
#   : 스크립트 실행중 불가항력의 상화에 따라 스크립트가 비정상 종료되는 상황을 정상적으로 종료될 수 있게하는 제어문
#
# error 종류
#  - syntax error : 문법 오류
#  - link error : 함수 오류
#  - run-time error : logic 오류   *** -> 문제의 요구사항에 맞게끔 logic을 세워야 해결됨, 결과가 나오게끔 변경
#  - warning : error 가능성이 있다. -> 무시해도 되는지 해결해야 하는지 판단을 해야함
#
# 예외 상황 (error)
a, b = 5, 0
# c = a / b    # link, runtime, syntax 오류가 아님 / 실질적으로 0으로 나눌 수 없는 거기 때문에 불가항력적인 오류

# print( 4 + spam * 3 ) # NameError : name 'spam' is not defined -> 스팸이라는 변수가 없다고 뜸(지정하지 않아서),

# print( '2' + 2 ) # TypeError: can only concatenate str (not "int") to str -> 연산할 때 문자와 정수는 안됨
#------------------------------------------------------------------------------------------------------
# Print( "HEllo, World" ) # link 에러 (print함수는 p가 소문자임, 파이썬은 대문자 소문자 구분이 가능해서 에러가 뜸)

# print( 'Hello ) # SyntaxError '로 막지 않아서, 완성시키지 않아서 에러
'''
x = 0
try:                                  # 예외 발생 가능성이 있는 코드 블록을 묶어주는 역할, try: -> 블록안에 있는 코드에서 예외가 발생하면 해당 예외를 감지 할 수 있다.
    print( 1.0 / x )
except ZeroDivisionError:             # 예외가 감지되었을 때 수행되는 코드블록
    print( 'zero division exeption' )
    print( 'stop script' )
'''

'''
try:
    print( '2' +2 )
except TypeError:                         
    print( '연산시 자료형이 맞지 않습니다.' )
    print( 'stop script' )
'''

'''
name = 'filename'
try:
    f = open( name, 'r' )
except IOError:                                         # 예외가 발생 했을 때
    print( name + '파일을 열수 없습니다.' )
    print( 'stop script' )
else:                                                   # 예외가 발생하지 않았을 때
    print( name, 'has', len( f.readline() ), 'lines' )
    f.close()
finally:                                                 # 예외와 상관없이 항상 수행되는 코드블록을 쓰는 곳
    print('예외와 상관없이 항상 수행하는 내용을 정의한다.')
'''
try:
    spam()
except NameError:
    print( 'Exeption : NameError' )
except TypeError:
    print( 'Exeption : TypeError' )
except ImportError:
    print( 'Exeption : IOError' )
except:         # 모든 예외를 감지 (이름을 정하지 않아도, 맨앞에 쓰면 그 밑으로는 다른 예외들이 의미가 없으므로 다른 예외를 쓰면 오류)
    print('Exeption 발생으로 스크립트 종료')
















