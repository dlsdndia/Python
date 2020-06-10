#
# 반복구조
# 1. for문 : 반복 횟수가 일정한 경우 사용
# 2. while문 : 반복 횟수가 일정하지 않은 경우 사용
#
# 1. for 문                                          list
# for < 반복제어변수 > in < 반복을 횟수를 결정하는 객체( sequence 형 ) >:
#    < 반복 수행 내용 >   --> 길이만큼 반복
#
l = [ 'cat', 'cow', 'tiger' ]
print( 'l : {}( {} )\n'.format( l, len( l ) ) )

for value in l:
    print( 'value : {}( {} )'.format( value, len( value ) ) )    # 길이만큼 반복이니까 tiger에서 끝남

print()
for i in range( 0, len( l ), 1 ):          # range ( 시작값, 끝값, 증가값 ) -> 0부터 3전까지 1씩 증가해라 / 시작값과 증가값을 안쓰면 0과 1이 고정이다.
    print( i, end = '\t')
    print('value : {}( {} )'.format(l[ i ], len( l[ i ] ) ) )


print()
for i in range( 1, 11, 1 ):
    print( i, end= ' ' )
print()

str = 'Python is great!!!'    # 반복횟수를 문자열 그대로 써서 그 값 그대로 사용
for value in str:
    print( value, end= ' ' )
print()

for i in range( len( str ) ):  # 반복횟수를 길이로 조정하여 사용
    print( str[ i ], end= ' ' )
print()

t = ( 100, 'hello', True, 'Hong' )
print( '\nt, : {}( {} )\n'.format( t, len( t ) ) )

for value in t:
    print( value, end= ' ' )
print()

for i in range( len( t ) ):
    print( t[ i ], end= ' ' )
print()

# enumerate() : 요소의 값과 인덱스를 제공하는 함수
#            (인덱스, 요소값 ) 형식으로 tuple 제공
for i, value in enumerate( l ):
    print( 'i : {}\tvalue : []'.format( i, value ) )
print()

# break : 반복을 탈출할 때 사용
# continue : 반복 조건 검사 수행
for i in range( 1, 101, 1 ):   # 1~101까지 100번 반복하라는 것
    if ( i % 10 ) == 0:        # i를 10으로 나누었을 때 나머지가 0이면 ->10의 배수
        continue               # 계속 하라 continue를 만나면 다시 위에 for문으로 간다. 즉 명령문 실행 안하고 건너뛰는 것
    if ( i >= 20 ):            # i가 20보다 크거나 같으면 break
        break                  # 반복 끝
    print( '{:5d}'.format( i ), end= '' )
# 반복문에는 선택 구조가 왠만하면 안들어가는게 좋음

#
# 2. while 문
#
# 반복제어변수 초기화   -> 초기값을 정해야함
# while < 반복탈출조건 >:      -> 참인동안 반복
#    < 반복수행내용 >
#   반복 제어 변수 변화
#
print()
i = 1                    # 반복 제어 변수 초기화
while i <= 10:           # 반복 탈출 조건 검사
    print( i, end= ' ' )
    i +=1                # 반복 제어 변수 변화    -> 탈출조건을 제어해줘야 함
print()

i = 1
while True:               # 추천방법은 아님
    if ( i > 10 ):
        break;
    print( i, end= ' ' )
    i += 1
print()

# 반복횟수를 입력값으로 제한
str = input( 'Input string ( quit : "end" ) : ' )    # 입력값이 end값이 나올때까지 반복 / 대문자 END
while str.lower() != 'end':
    print( '[{:3d}] : {}'.format( i, str ) )
    i += 1
    str = input( 'Input string ( quit : "end" ) : ' )

str = input( 'Input string ( quit : "end" ) : ' )    # 입력값이 end값이 나올때까지 반복
while str != 'end':                                  # 대문자도 입력하게 하려면 위에처럼
    print( '[{:3d}] : {}'.format( i, str ) )
    i += 1
    str = input( 'Input string ( quit : "end" ) : ' )









