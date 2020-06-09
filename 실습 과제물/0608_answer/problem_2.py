#
# 2) 다섯 정수를 입력받아 평균, 편차, 편차제곱, 분산을 출력하는 파이썬 스크립트
#
# 0. 필요 변수 선언( 변량의 수 )
count = 0

# 1. 다섯 정수 입력
number1 = int( input( "Input number1 : " ) )
count += 1                                          # 갯수가 늘어날때마다 1이 더해짐

number2 = int( input( "Input number2 : " ) )
count += 1

number3 = int( input( "Input number3 : " ) )
count += 1

number4 = int( input( "Input number4 : " ) )
count += 1

number5 = int( input( "Input number5 : " ) )
count += 1

# 2. 평균 계산
mean = ( number1 + number2 + number3 + number4 + number5 ) / count  # count만 하면 변수가 5개있어서 있어서 5가 자동으로 적용

# 3. 편차 계산
deviation1 = number1 - mean
deviation2 = number2 - mean
deviation3 = number3 - mean
deviation4 = number4 - mean
deviation5 = number5 - mean

# 4. 편차 제곱 계산
deviation_squared1 = deviation1 * deviation1
deviation_squared2 = deviation2 * deviation2
deviation_squared3 = deviation3 * deviation3
deviation_squared4 = deviation4 * deviation4
deviation_squared5 = deviation5 * deviation5

# 5. 분산 계산
variance = ( deviation_squared1 + deviation_squared2 + deviation_squared3 + deviation_squared4 + deviation_squared5 ) / count

# 6. 출력
print( '\nnumber1 = {0:5}\nnumber2 = {1:5}'.format( number1, number2 ) )
print( 'number3 = {0:5}\nnumber2 = {1:5}'.format( number3, number4 ) )
print( 'number1 = {0:5}\n'.format( number5 ) )

print( 'mean = {:8.2f}\n'.format( mean ) )

print( 'deviation1 = {0:5}\ndeviation2 = {1:5}'.format( deviation1, deviation2 ) )
print( 'deviation3 = {0:5}\ndeviation4 = {1:5}'.format( deviation3, deviation4 ) )
print( 'deviation5 = {0:5}\n'.format( deviation5 ) )

print( 'deviation_squared1 = {0:5}\ndeviation_squared2 = {1:5}'.format( deviation_squared1, deviation_squared2 ) )
print( 'deviation_squared3 = {0:5}\ndeviation_squared4 = {1:5}'.format( deviation_squared3, deviation_squared4 ) )
print( 'deviation_squared5 = {0:5}\n'.format( deviation_squared5 ) )

print( 'variance = {:8.2f}\n'.format( variance ) )
