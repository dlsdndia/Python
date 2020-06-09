#
# 1) 두 정수를 입력 받아 합계, 평균을 출력하는 파이썬 스크립트
#
# 1. 두 정수 입력
number1 = int( input( "Input number1 : " ) )
number2 = int( input( "Input number2 : " ) )

# 2. 합계, 평균 계산
total = number1 + number2
average = total / 2

# 3. 출력
print( '\nnumber1 = {0:5}\nnumber2 = {1:5}\n'.format( number1, number2 ) )
print( 'total = {:10}'.format( total ) )
print( 'average = {:8.2f}'.format( average ) )
