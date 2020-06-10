#
# 3) 두 정수를 입력 받아 합계, 평균을 출력하는 파이썬 스크립트( list 이용 )
#
# 0. 두 정수 저장 list 생성
numbers = []

# 1. 두 정수 입력
number = int( input( "Input number1 : " ) )
numbers.append( number )
number = int( input( "Input number2 : " ) )
numbers.append( number )

# 2. 합계, 평균 계산
total = numbers[ 0 ] + numbers[ 1 ]
average = total / 2

# 3. 출력
print( '\nnumber1 = {0:5}\nnumber2 = {1:5}\n'.format( numbers[ 0 ], numbers[ 1 ] ) )
print( 'total = {:10}'.format( total ) )
print( 'average = {:8.2f}'.format( average ) )
