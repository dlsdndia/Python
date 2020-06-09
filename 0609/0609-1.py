#
# 문자열
#    : 문자 집합
#    : sequence 자료형     -->> 순서가 존재한다.
#    : 인덱싱, 슬라이싱, 결합, 반복, 멤버 검사, 길이 계산의 sequence자료형
#    : 공통 연산을 적용할 수 있다.
# 문자열 생성
str = ''
str2 = 'hello'
print( 'type(str) : ', type( str ), end='' )
print( '\ttype(str2) : ', type(str2) )
print( 'str : {}\tstr2 : {}\n'.format( str, str2 ) )

str = 'Don\'t walk. "Run"'                   #'를 문자에서 '를 쓸 때 앞에 역슬레시 \를 써줌
print(str)

str = ' this is a rather long string \
containing back slash and Line.\nGood!'
print( str )

str = '''
Python is great!\nyes, it is.   
'''

print( str, '\n' )

str = ' this is a rather long string ' + \
      'containing back slash and Line.\nGood!'
print( str, '\n' )


# 문자열 길이 계산
str = "Python is great!!!"
print( "str : {}\tlength : {}\n".format( str, len( str ) ) )

# 문자열 내용 포함 확인
print( "P" in str )
print( 'p' in str )
print( 'Python' in str )
print( 'is' in str )
print( 'th' in str, '\n' )

# 문자열 인덱싱 : 파이썬에서 인덱싱 시작은 [ 0 ]부터 마지막은 [ 길이 - 1 ]  ex) 0, 1, 2, 3, 4~~
#     : 문자열의 원하는 문자에 접근하는 방법
print( str[ 0 ] )
print( str[ 7 ] )
print( str[ -1 ] )             # 파이썬에서 -는 역순서 즉, -1은 끝에서 2번째
print( str[ -8 ], '\n' )

# 문자열 슬라이싱 : 문자열에 대하여 부분 문자를 지정할 때 사용
print( str[ 0:6 ] )             # 0부터 6까지 이지만 6은 포함은 안됨
print( str[ 8:10 ] )
print( str[ 7:12:3 ] )          # 7부터 11번째까지 3번씩 증가한값의 값이 나와라 즉 7, 10만
print( str[ :6 ] )              # 시작부터 ~ 5번째 까지
print( str[ 11: ] )
print( str[ ::2 ] )             # 처음붕터 끝까지 2씩 증가하는 값이 나와라 0, 2, 4~~~
print( str[ ::-1 ] )            # 역순으로
print( str[ : ] )               # 전체
print( str[ -50:50 ], '\n' )    # 원래 범위를 벗어나면 전체가 나옴

# 문자열은 변경 불가 자료형
# str[ 0 ] = 'p'      str 0번째를 p로 바꿔라 하지만 자료형이 변경 불가형 자료형이라 안됨
print( str, '\n' )

# 문자열 결합( + )
s1 = 'first'
s2 = 'second'
s3 = s1 + ' ' + s2
print( "s1 : [ {} ] s2 : [ {} ] s3 : [ {} ]\n".format( s1, s2, s3 ) )

# 문자열 반복( * )
print( s1 * 3, '\n' )

s = 'spam and egg'
print( s )
s = s[ :5 ] + 'cheese' + s[ 5: ]
print( s )

# 문자열 함수
str = 'i like programing. i like swimming'
print( '\n' + str.upper() )           # 전체 대문자
print( str.lower() )                  # 전체 소문자
print( str.capitalize() )             # 가장 첫번째 글자만 대문자
print( str.title() )                  # 단어의 첫글자를 대문자로
print( str.count( 'like') )           # 해당 단어가 몇번 나왔는지
print( str.find( 'like' ) )           # 해당 단어의 위치 (앞에서부터 몇번째이냐)
print( str.rfind( 'like' ) )          # rfind = right 오른쪽에서 부터 like 위치

str = ' spam and egg '
print( str.strip() )                  # 앞, 뒤 공백을 없애라
print( str.rstrip() )
print( str.split() )                  # split= 자르다, 공백을 기준으로 앞뒤를 자른것
print( str.split( 'and' ), '\n' )           # and를 기준으로 앞뒤를 자른 것

l = str.split()
print( ':'.join( l ) )                # join은 결합, split한걸 다시 결합하는데 :을 붙여서 하겠다.
print( '\n'.join( l ), '\n' )
print( str.center( 60 ) )             # 전체 폭을 60으로 잡고 그곳에 중간에 놓겠다.
print( str.ljust( 60 ) )              # 전체 폭을 60으로 잡고 왼쪽으로 정렬
print( str.rjust( 60 ) )
print( str.center( 60, '-' ) )        # 전체 폭 60에서 가운데에 정렬하고 나머지는 -로 출력

print( ord( 'A' ) )                   # ASCII 코드값 -> ord에 문자를 주면 해당하는 십진수를 줌
print( chr( 0x0041 ) )                # ASCII 코드값의 문자
































































