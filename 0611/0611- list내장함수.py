#
# list comprehensien( list 내장 )
#          : 기능은 별도의 제어문을 사용하지 않고 반복 기능을 활용하여 list값을 저장하는 방법
# for문을 이용하여 list에 1~10까지 값 저장
l = []
for i in range( 1, 11):
    l.append( i )
print( 'l : {}( {} )\n'.format( l, len( l ) ) )

# list comprehension 이용하여 list에 1~10까지 값 저장
l2 = [ i for i in range( 1, 11 ) ]
print( 'l2 : {}( {} )\n'.format( l2, len( l2 ) ) )

l = []
for i in range( 1, 11 ):
    if i % 2 == 0:
        l.append( i )
print( 'l : {}( {} )\n'.format( l, len( l ) ) )

l2 = [ i for i in range( 1, 11 ) if i % 2 == 0 ]
print( 'l2 : {}( {} )\n'.format( l2, len( l2 ) ) )


# 1~1000사이의 3의 배수 이거나 5의 배수를 list comprehension을 이용하여 기억시켜라
l = [ i for i in range( 1, 1001 ) if i % 3 == 0 or i % 5 == 0 ]
print( 'l : {}( {} )\n'.format( l, len( l ) ) )

# list에 양수/음수/짝수/홀수를 섞어서 저장한 후
# list comprehension을 이용하여 양수/음수, 양수일 때 짝수/홀수
# 갯수 출력
l = [ 5, -9, 7, 4, 10, -17, 12, 0, 24, -77 ]
print( 'l : {}( {} )\n'.format( l, len( l ) ) )

positive = [ value for value in l if value > 0 ]
negative = [ value for value in l if value < 0 ]
print( 'positive : {}( {} )\n'.format( positive, len( positive ) ) )
print( 'negative : {}( {} )\n'.format( negative, len( negative ) ) )

even = [ value for value in positive if value % 2 == 0 ]    # 이거랑
odd = [ value for value in positive if value % 2 != 0 ]
print( 'even : {}( {} )\n'.format( even, len( even ) ) )
print( 'odd : {}( {} )\n'.format( odd, len( odd ) ) )

even = [ value for value in l if value > 0 and value % 2 == 0 ] # 이거랑 같음 간편한게 좋음
print( 'even : {}( {} )\n'.format( even, len( even ) ) )

# 중첩 반복을 이용한 list comprehension
str1 = 'Hello'
str2 = 'World'

l = []
for v1 in str1:
     for v2 in str2:
         l.append( v1 + v2 )
print( 'l : {}( {} )\n'.format( l, len( l ) ) ) # for구문으로 한 것

l = [ v1 + v2 for v1 in str1 for v2 in str2 ]   # 중첩 반복으로 이용한 것
print( 'l : {}( {} )\n'.format( l, len( l ) ) )

# list comprehension을 이용한 1~9까지의 구구단표
multiple_table = [ i * j for i in range( 1, 10 ) for j in range( 1, 10 ) ] #
print( multiple_table )
count = 1
for value in multiple_table:
    print( '{:3d}'.format( value ), end = '' )
    count += 1
    if count > 9:
        print()
        count = 1

# list comprehenseion을 이용한 2차원 list
multiple_table = [ [ i * j for i in range( 1, 10 ) for j in range( 1, 10 ) ] ]   # 대괄호가 2개 들어가면 2차원 형태
print( '\nmultiple_table : {}( {} )\n'.format( multiple_table, len( multiple_table ) ) ) # 위에 두개와 같은 것을 줄바꿈 안함 것
print()

for multiple in multiple_table:
    for value in multiple:
        print('{:3d}'.format(value), end='')
    print()

words = ' the quick brown fox jumps over the lazy dog'.split()
print( 'word : {}( {} )\n'.format( words, len( words ) ) )
stuff = [ [ w.upper(), w.lower(), len( w ) ]for w in words ] # 대괄호가 2개면 2차원 형태
print( 'stuff : {}'.format( stuff ) )

for word in stuff:
    print( word)

str1 = [ 'A', 'B', 'C' ]
str2 = [ 'D', 'E', 'F' ]
l1 = [ i + j for i in str1 for j in str2 ]           # 1차원 만드는 컴프리핸션
l2 = [ [ i + j for i in str1 ] for j in str2 ]       # 2차원 만드는 컴프리핸션
print( '\nl1 : {}( {} )'.format( l1, len( l1 ) ) )   # 1차원 형태 (열의 집합)
print( 'l2 : {}( {} )'.format( l2, len( l2 ) ) )# 2차원 형태 ( 행, 열의 집합 ) / 밑줄(한층)이 1차원 2,3층이 생기면 2차워
print()
#l2 : [['AD', 'BD', 'CD'], ['AE', 'BE', 'CE'], ['AF', 'BF', 'CF']]( 3 )
#  [[0행0열, 0행1열, 0행2열]], [[]]
# 대괄호 하나 썼을 때와 두개 썼을 대의 차이를 잘봐라


# dictionary comprehension
# ecumerate() : list에 대하여 ( index, value ) 형식으로 나열하는 함수
str = [ 'apple', 'banana', 'pineapple', 'melon' ]
for index, value in enumerate( str ):
    print( '[ {:2d} ] {:<20s}'.format( index, value ) )
print()

# str의  index 사용
for index in range( len(str ) ):                                    # 1      list길이를 이용하여 반복
    print( '[ {:2d} ] {:<20s}'.format( index, str[ index ] ) )

print()
for s in str:                                                       # 2      list자체를 이용하여 반복, list요소(내용, 값)
    print( '{:<20s}'.format( s ) )
print()
for index, value in enumerate( str ):                               # 3             1,2,3 차이 알기
    print( '[ {:2d} ] {:<20s}'.format( index, value ) )

for index, _ in enumerate( str ):                                   # 이것과 / enumerate함수 쓰임 알기
    print( '[ {:2d} ] {:<20s}'.format( index, str[ index ] ) )

for _ in range( 1, 6 ):                                             # 이것은 단지 목적이 단지 반복일 때 반복제어이름이 필요없을 때
    print( 'Hello!!!')
print()

# zip() : sequence형(리스트) 값을 병렬로 묶는 함수
l = [ 1, 2, 3 ]
str = [ 'apple', 'banana', 'pineapple' ]
for index, value in zip( l, str ):                     # zip으로 묶을 때 같은 위치끼리 묶임
    print( '[ {:2d} ] {:<10s}'.format( index, value ) )
print()

a, b, c = zip( ( 1, 2, 3 ), ( 10 ,20 ,30 ), ( 100, 200, 300 ) )  # [0][0]과 [1][0]이런식으로 묶임 같은 자리 끼리
print( a, b, c, '\n' )

str1 = [ 'a1', 'a2', 'a3' ]
str2 = [ 'b1', 'b2', 'b3' ]
for index, value in enumerate(zip( str1, str2 ) ):
    print( '[ {:2d} ] {}'.format( index, value ) )


# dictionary comprehension
print()
d = { w:1 for w in 'abc' } # {}는 딕션생성할 때 / w = key , value = 1
print( d )
print()

str = 'abce'
t = ( 1, 2, 3, 4 )
d = { k:v for k, v in zip( t, str ) }
print( d )
print()

d = { k:v for k, v in [ ( 1, 'one' ), ( 2, 'two' ), ( 3, 'three' ) ] } # 튜플로 구성된 list
print( d )
print()

d = { v:k + 1 for k, v in enumerate( [ 'one', 'two', 'three' ] ) }    # v:k +1은 내가 key값을 0으로 쓰지 않겠따는 것
print( d )
print()

print( d.items() )                 # key, value를 다 가져오는 함수 .items()
d2 = { v:k for k, v in d.items() }
print( d2 )
print()

d = { ( k, v ): k + v for k in range( 3 ) for v in range( 3 ) }
print( d )














