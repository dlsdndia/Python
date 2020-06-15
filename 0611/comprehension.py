#
# list comprehension( list 내장 )
#   : comprehension( 내장 ) 기능은 별도의 제어문을 사용하지 않고 반복 기능을
#     활용하여 list에 값을 저자하는 방법
# for문을 이용하여 list에 1~10까지 값 저장
l = []
for i in range( 1, 11 ):
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

# 1~1000사이의 3의 배수 이거나 5의 배수를 list comprehension을
# 이용하여 기억시켜라
l = [ i for i in range( 1, 1001 ) if i % 3 == 0 or i % 5 == 0 ]
print( 'l : {}( {} )\n'.format( l, len( l ) ) )

# list에 양수/음수/짝수/홀수를 썩어서 저장한 후
# list comprehension을 이용하여 양수/음수, 양수일 때 짝수/홀수
# 갯수 출력
l = [ 5, -9, 7, 4, 10, -17, 12, 0, 24, -77 ]
print( 'l : {}( {} )\n'.format( l, len( l ) ) )

positive = [ value for value in l if value > 0 ]
negative = [ value for value in l if value < 0 ]
print( 'positive : {}( {} )'.format( positive, len( positive ) ) )
print( 'negative : {}( {} )'.format( negative, len( negative ) ) )

even = [ value for value in positive if value % 2 == 0 ]
odd = [ value for value in positive if value % 2 != 0 ]
print( 'even : {}( {} )'.format( even, len( even ) ) )
print( 'odd : {}( {} )\n'.format( odd, len( odd ) ) )

even = [ value for value in l if value > 0 and value % 2 == 0 ]
print( 'even : {}( {} )\n'.format( even, len( even ) ) )

# 중첩 반복을 이용한 list comprehension
str1 = 'Hello'
str2 = 'World'

l = []
for v1 in str1:
    for v2 in str2:
        l.append( v1 + v2 )
print( 'l : {}( {} )\n'.format( l, len( l ) ) )

l = [ v1 + v2 for v1 in str1 for v2 in str2 ]
print( 'l : {}( {} )\n'.format( l, len( l ) ) )

# list comprehension을 이용한 1~9까지의 구구단표 저장 후 출력
multiple_table = [ i * j for i in range( 1, 10 ) for j in range( 1, 10 ) ]
print( multiple_table )
count = 1
for value in multiple_table:
    print( '{:3d}'.format( value ), end = '' )
    count += 1
    if count > 9:
        print()
        count = 1

# list comprehension을 이용하 2차원 list
multiple_table = [ [ i * j for i in range( 1, 10 ) ] for j in range( 1, 10 ) ]
print( '\nmultiple_table : {}( {} )\n'.format( multiple_table, len( multiple_table ) ) )

for multiple in multiple_table:
    for value in multiple:
        print( '{:3d}'.format( value ), end = '' )
    print()

words = 'The quick brown fox jumps over the lazy dog'.split()
print( 'words : {}( {} )'.format( words, len( words ) ) )
stuff = [ [ w.upper(), w.lower(), len( w ) ] for w in words ]
print( 'stuff : {}'.format( stuff ) )

for word in stuff:
    print( word )

str1 = [ 'A', 'B', 'C' ]
str2 = [ 'D', 'E', 'F' ]
l1 = [ i + j for i in str1 for j in str2 ]
l2 = [ [ i + j for i in str1 ] for j in str2 ]
print( '\nl1 : {}( {} )'.format( l1, len( l1 ) ) )
print( 'l2 : {}( {} )'.format( l2, len( l2 ) ) )

# dictionary comprehension
# enumerate() : list에 대하여 ( index, value ) 형식으로 나열하는 함수
str = [ 'apple', 'banana', 'pineapple', 'melon' ]

# str의 index 사용
for index in range( len( str ) ):       # list 길이를 이용하여 반복, index 사용
    print( '[ {:2d} ] {:<20s}'.format( index, str[ index ] ) )
print()

for s in str:                           # list 자체를 이용하여 반복, list 요소( 내용, 값 )
    print('{:<20s}'.format( s ) )
print()

for index, value in enumerate( str ):
    print( '[ {:2d} ] {:<20s}'.format( index, value ) )
print()

for index, _ in enumerate( str ):
    print( '[ {:2d} ] {:<20s}'.format( index, str[ index ] ) )

for _ in range( 1, 6 ):
    print( 'Hello!!!' )

# zip() : 리스트( sequence형 ) 값을 병렬로 묶는 함수
l = [ 1, 2, 3 ]
str = [ 'apple', 'banana', 'pineapple' ]
for index, value in zip( l, str ):
    print( '[ {:2d} ] {:<10s}'.format( index, value ) )
print()

a, b, c = zip ( ( 1, 2, 3 ), ( 10, 20, 30 ), ( 100, 200, 300 ) )
print( a, b, c, '\n' )

str1 = [ 'a1', 'a2', 'a3' ]
str2 = [ 'b1', 'b2', 'bd' ]
for index, value in enumerate( zip( str1, str2 ) ):
    print('[ {:2d} ] {}'.format(index, value))

# dictionary comprehension
d = { w:1 for w in 'abc' }
print( d )

str = 'abce'
t = ( 1, 2, 3, 4 )
d = { k:v for k, v in zip( t, str ) }
print( d )

d = { k:v for k, v in [ ( 1, 'one' ), ( 2, 'two' ), ( 3, 'three' ) ] }
print( d )

d = { v:k + 1 for k, v in enumerate( [ 'one', 'two', 'three' ] ) }
print( d )

print( d.items() )
d2 = { v:k for k, v in d.items() }
print( d2 )

d = { ( k, v ): k + v for k in range( 3 ) for v in range( 3 ) }
print( d )
