#
# 4) 다섯 정수를 입력받아 평균, 편차, 편차제곱, 분산을 출력하는 파이썬 스크립트( list 이용 )
#
# 0. 다섯 정수 저장 list 생성
numbers = []

# 1. 다섯 정수 입력
# 1.1 입력된 정수를 list에 저장
number = int( input( "Input number1 : " ) )
numbers.append( number )

number = int( input( "Input number2 : " ) )
numbers.append( number )

number = int( input( "Input number3 : " ) )
numbers.append( number )

number = int( input( "Input number4 : " ) )
numbers.append( number )

number = int( input( "Input number5 : " ) )
numbers.append( number )

# 1.2 인원수 저장
count = len( numbers )

# 2. 평균 계산
sum = numbers[ 0 ] + numbers[ 1 ] + numbers[ 2 ] + numbers[ 3 ] + numbers[ 4 ]
mean = sum / count

# 3. 편차 계산
deviation1 = numbers[ 0 ] - mean
deviation2 = numbers[ 1 ] - mean
deviation3 = numbers[ 2 ] - mean
deviation4 = numbers[ 3 ] - mean
deviation5 = numbers[ 4 ] - mean

# 4. 편차 제곱 계산
deviation_squared1 = deviation1 * deviation1
deviation_squared2 = deviation2 * deviation2
deviation_squared3 = deviation3 * deviation3
deviation_squared4 = deviation4 * deviation4
deviation_squared5 = deviation5 * deviation5

# 5. 분산 계산
variance = ( deviation_squared1 + deviation_squared2 + deviation_squared3 + deviation_squared4 + deviation_squared5 ) / count

# 6. 출력
print( '\nnumber1 = {0:5}\nnumber2 = {1:5}'.format( numbers[ 0 ], numbers[ 1 ] ) )
print( 'number3 = {0:5}\nnumber4 = {1:5}'.format( numbers[ 2 ], numbers[ 3 ] ) )
print( 'number5 = {0:5}\n'.format( numbers[ 4 ] ) )

print( 'mean = {:8.2f}\n'.format( mean ) )

print( 'deviation1 = {0:5.2f}\ndeviation2 = {1:5.2f}'.format( deviation1, deviation2 ) )
print( 'deviation3 = {0:5.2f}\ndeviation4 = {1:5.2f}'.format( deviation3, deviation4 ) )
print( 'deviation5 = {0:5.2f}\n'.format( deviation5 ) )

print( 'deviation_squared1 = {0:5.2f}\ndeviation_squared2 = {1:5.2f}'.format( deviation_squared1, deviation_squared2 ) )
print( 'deviation_squared3 = {0:5.2f}\ndeviation_squared4 = {1:5.2f}'.format( deviation_squared3, deviation_squared4 ) )
print( 'deviation_squared5 = {0:5.2f}\n'.format( deviation_squared5 ) )

print( 'variance = {:8.2f}\n'.format( variance ) )
