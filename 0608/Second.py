'''
    파이썬 자료형
          * 원시 자료형 (원자적인 성격, 더이상 분해가 안되는 성격)
          숫자형 : int, float, complex (산술연산이 가능함), 정수, 실수, 복소수
          논리형 : bool
          바이트형 : byte, 1byte문자 (무조건 글자 하나에 1byte로 하는 것), 주로 통신 때문에

          # 집합 자료형 ( 원시 자료형이 모인 것 )

           # sequence형
           문자형 : str ( 문자 집합 )
           배열 : list ( 값으 집합 ), 정수값의 집합 등, 수정이 필요할 때 사용
           배열(수정불가) : tuple(튜플), 한벙 정하면 값을 못 바꿈, 수정을 하면 안되는 것을 할 때

           # mapping
           배열(key:value 형식) : dict => R에서의 형식, 키:값

           # set형
           집합 : set -> 중복을 허용하지 않음(값의 중복)

'''

# 원시 자료형
intNumber1 = 10
intNumber2 = 5
floatNumber1 = 12.9;     floatNumber2 = 3.2   # 한줄에 원래 명령 하나이지만 여러개 쓸 때 ;를 쓰기
boolVariable = True
variable = None   # null과 같은 뜻 아무것도 없다는 뜻, 아무것도 없다의 뜻, 값이 없다, 자료형도 결정 안됨, none type = 형이 없음
bytValiable = b'python' #-> b''면  ''안에 글자를 1byte로 인식

print( intNumber1, '\t', intNumber2 )       # \t -> 제어문자 = 탭간격으로 띄움 \n은 줄바꿈
print( type( intNumber1 ), '\t', type( intNumber2 ) )
print( floatNumber1, '\t', type( floatNumber2 ) )
print( type( floatNumber1 ), '\t', type( floatNumber2 ) )
print( boolVariable )
print( type( boolVariable ) )
print( variable )
print( type( variable ) )
print( bytValiable )
print( type( bytValiable ) )


print()
# 정수형
number = 23  #10진 정수
print( number, '\t', type( number ) ) #
binary = 0b1101    # 2진 정수
octal = 0o23       # 8진 정수
hexa = 0x23        # 16진 정수
print( number, '\t', binary, '\t', octal, '\t', hexa )
print( 2 ** 1024 )  # 정수 범위에 제한이 없다.(파이썬은 정수 범위가 제한 없음)

# 정수 형변환
print()
print( int( '23', 8 ) ) # 문자열을 정수로 바꾸는 것, 문자열이 8진수
print( int( '123' ) )   # 문자열을 정수로 변환
print( int( 2.9 ) )     # 실수를 정수로 변환
print( int( float( '123.45' ) ) )      # 문자열을 실수로 변환한 후 다시 정수로 변환

print()
print( bin( 23 ) )    # 2진수로 변환
print( oct( 23 ) )    # 8진수로 변환
print( hex( 23 ) )    # 16진수로 변환


# 실수
print()
fnumber = 1.2
print( fnumber, '\t', type( fnumber ) )
fnumber2 = 3e+3        # 지수표현, 과학적 표기법 , e라는 기호가 붙으면 지수로 표현 3e+3 = > 0이 3개
print( fnumber2, '\t', type( fnumber2 ) )

print()
print( round(1.2 ) )  # round 함수는 반올림
print( round(1.0 ) )

#무한대 표현 (정수말고 실수에 보통 적용)     파이썬은 아주 정밀한 연산에 오차가 있어서 정말 정밀한 계산에는 유의
print()
print( float( 'inf' ) )  # inf는 무한대로 표현하는 것 , 양수 무한대로 표현 float()애는 문자열이 들어가면
                          # 안되는데 무한대를 나타내는 'inf'만 가능
print( float( '-inf' ) )  # 음수 무한대로 표현
infinity = float( 'inf' )
print( infinity / 1000 )


# 논리형
print()
number = 1
print( number < 0 )
print( number > 0 )

print( True + True )   # true = 1
print( True + False )  # false = 0
print()

print( bool( 1 ) )     # 0만 아니면 다른 숫자는 다 true
print( bool( 0 ), '\t', bool( None ), '\t', bool( ' ' ) )   # 숫자 0 , None값일 때, 값이 없을 때 는 모두 다 false
                                                           # ' ' 안에 공백을 넣으면 true


# 바이트형
print()
byteVariable = b'Python'
print( byteVariable, '\n', type( byteVariable ) )
print( byteVariable > 0 )   # 논리형에는 맞지 않아서 값이 안나옴

print()
s = '홍길동'
# b = b'홍길동' # 1바이트로 바꾸는 건데 한글은 2바이트로만 가능하기 때문에 오류가 남, ASCII만 써야 함, 통신프로그램으 짤때는 이 byte를 써야함


# 에러 종류
# SyntaxError = 문법 오류
# LInkError = 함수 오류
# Run-TimeError = 결과 오류
# Warning = 지금은 오류가 없지만 오류 가능성이 있다.






























