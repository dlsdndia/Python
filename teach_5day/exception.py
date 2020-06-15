#
# 예외 처리( Exception )
#   : 스크립트 실행중 불가항력의 상황에 따라 스크립트가 비정상 종료되는
#     상황을 정상적으로 종료될 수 있게하는 제어문
#
# 예외 상황
a, b = 5, 0
#c = a / b      # ZeroDivisionError : division by zero 라는 exception

#print( 4 + spam * 3 ) # NameError : name 'spam' is not defined

#print( '2' + 2 ) # TypeError: can only concatenate str (not "int") to str

#Print( "Hello, World" ) # Link Error

#print( 'Hello ) # Syntax Error

'''
x = 0
try:   # 예외 발생 가능성이 있는 코드 블록을 묶어주는 역활
       # try: 블록안에 있는 코드에서 예외가 발생하면 해당 예외를 감지
       # 할 수 있다.
    print( 1.0 / x )
except ZeroDivisionError: # 예외가 감지되었을 때 수행되는 코드블록
    print( 'zero division exception' )
    print( 'stop script' )
'''

'''
try:
    print( '2' + 2 )
except TypeError:
    print( '연산시 자료형이 맞지 않습니다.' )
    print( 'stop script' )
'''

'''
name = 'filename'
try:
    f = open( name, 'r' )
except IOError: # 예외가 발생했을때 처리 내용
    print( name + ' 파일을 열수 없습니다.' )
    print( 'stop script' )
else: # 예외가 발생하지 않았을 때 처리
    print( name, 'has', len( f.readline() ), 'lines' )
    f.close()
finally: # 예외가 발생하거나 발생하지 않거나 항상 수행되는 코드블록
    print( '예외와 상관없이 항상 수행하는 내용을 정의한다.' )
'''

try:
    spam()

except NameError:
    print( 'Exception : NameError' )
except TypeError:
    print('Exception : TypeError')
except IOError:
    print('Exception : IOError')
except: # 모든 예외 감지
    print('Exception 발생으로 스크립트 종료' )



