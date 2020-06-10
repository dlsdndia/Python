#
# tuple
#    : 수정 불가능한 데이터 집합, 데이터 저장
#    : sequence 자료형
#    : 인덱싱, 슬라이싱, 결합, 반복, 멤버 검사, 길이 계산의 sequence 자료형
#    : 공통 연산을 적용할 수 있다.
#    : 출력될 때 가로로 묶여나오면 튜플이라고 보면 된다.
#    : 튜플은 ,가 있어야 함 ,가 없으면 튜플이 아니고 값임 하나여도 ,가 뒤에 찍힘 / 튜플의 특징
# tuple 생성
t = () # 빈 튜플
print( 't : {}\tlen( t ) : {}'.format( t, len( t ) ) )

t = ( 1, 2, 3 )
print( 't : {}\tlen( t ) : {}'.format( t, len( t ) ) )

t = 1, 2, 3                                                # 가로가 없어도 ,가 있으면 튜플로 인식
print( 't : {}\tlen( t ) : {}'.format( t, len( t ) ) )

t = ( 1, )
print( 't : {}\tlen( t ) : {}'.format( t, len( t ) ) )

t = 1,
print( 't : {}\tlen( t ) : {}\n'.format( t, len( t ) ) )


# 튜플 내용 포함 확인
t = ( 1, 2, 3 )
print( 1 in t )
print( 5 in t, '\n' )

# 튜플 인덱싱
print( t[ 0 ] )
print( t[ 2 ] )
print( t[ -2 ], '\n' )

# 튜플 슬라이싱
print( t[ 0:3 ] )
print( t[ 1:3 ] )
print( t[ 2: ] )
print( t[ :2 ] )
print( t[ ::2 ], '\n' )

# 튜플 결합
print( t + t, '\n' )

# 튜플 반복
print( t * 2, '\n' )

# 튜플 함수
t = ( 1, 2, 3, 2, 5, 1, 4, 3 )
print( t.count( 2 ) )
print( t.index( 2 ) )          # 해당하는 값의 위치
print( t.index( 2, 2 ) )       # (숫자1, 숫자2) -> 검색 시작위치(숫자1),

# 튜플 중첩
t1 = ( 1, 2, 3 )
t2 = ( "hello", 2020, 'world' )  # 튜플은 서로다른 자료형이 들어와도 가능
t = t1, t2
print( t )
print( t[ 0 ][ 1 ], '\n' )

t = (1, 2, 3 ), ( "hello", 2020, 'world' ), 10
print( t )
print( t[ 0 ] )
print( t[ 0 ][ : 2 ] )     # [ : 2 ] 는 시작부터 2번째 까지 :있을 때는 아마 0부터가 아니라 순서인 것 같다
print( t[ 2 ], '\n' )

# 튜플을 이용한 데이터 치환
x, y, z = 1, 2, 3                           # ,가 있으면 튜플 왼쪽 오른쪽 튜플이니까 왼쪽 순서 오른쪽 순으로 각각 치환된 것
print( x, y, z )
( x1, x2 ), ( y1, y2 ) = ( 1, 2 ), ( 3, 4 )
print( x1, x2, y1, y2, '\n' )

#순서 외우기( 값을 바꾸는 법 ), 컴퓨터 상에서 두 데이터를 교환하는 법 하지만 밑에
x, y = 1, 2
print( x, y )
t = x                  # 임시 데이터 저장소 데이터를 바꾸기 위한
x = y
y = t
print( x, y, '\n' )

# 파이썬에서는 이렇게 데이터를 바로 바꾸는 것이 가능하다
x, y = 1, 2
print( x, y )
x, y = y, x
print( x, y, '\n' )

# 패킹(packing) : 한 공간에 여러개의 데이터를 넣는 행위
# 언패킹( unpacking ) : 데이터 집합의 내용을 꺼오는 행위
t = 1, 2, 'python'  # 패킹
print( t )
x, y, z = t         # 언패킹
print( x, y, z, '\n' )

# 확장된 언패킹
# 확장된 언패킹에서 *의 의미는 전부라는 뜻
t = ( 1, 2, 3, 4, 5 )
print( t )
a, *b = t             # 순서대로 적용하는 듯  / 즉 변수의 개수가 같아야 하는데 *로 변수의 개수를 맞추니 언패킹이 가능한 것
print( a, b )
*a, b = t             # 마지막을 b로 보고 b말고 마지막 앞에꺼 전부 a
print( a, b )
a, b, *c = t
print( a, b, c )

# 튜플이 활용되는 경우
# 1. 함수에서 하나 이상의 값을
# 반환( retuen 값 ) 할 때 활용
# 2. 함수의 인수로 활용
# 3. 파이썬 2형식의 print() 형식 지정 출력에 사용























































