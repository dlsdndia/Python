#
# 2) -99999가 입력될 때까지 정수를 입력받아 평균을 계산하고, 편차, 편차제곱은
#    list comprehension을 이용하여 list에 저장한 후 분산을 계산하여 출력하는 파이썬 스크립트
# symbolic constant
END = -99999
MAX_LINE = 10

# 1. 변수 생성
numbers = []
total = 0
deviation_squareds_total = 0

# 2. 변량 입력
# 2.1 변량 입력
i = 1
number = int( input( "Input number[ %5d ] : " % ( i ) ) )
while number != END:
    numbers.append( number )
    total += number
    i += 1
    number = int(input("Input number[ %5d ] : " % ( i ) ) )

# 2.2 입력된 변량의 수 저장
count = len( numbers )

# 3. 평균 계산
mean = total / count

# 4. 편차 계산
deviations = [ value - mean for value in numbers ]

# 5. 편차 제곱 계산
deviation_squareds = [ value ** 2 for value in deviations ]

# 6. 분산 계산
for value in deviation_squareds:
    deviation_squareds_total += value
variance = deviation_squareds_total / count

# 7. 결과 출력
print()
line_count = 1
print( '\n변량 출력 :' )
for i in range( count ):
    print( '{:8}'.format( numbers[ i ] ), end = '' )
    line_count += 1
    if line_count > MAX_LINE:
        print()
        line_count = 1
print()

print( '\nmean = {:8.2f}\n'.format( mean ) )

print( '편차 출력 :' )
for i in range( count ):
    print( '{:8.2f}'.format( deviations[ i ] ), end = '' )
    line_count += 1
    if line_count > MAX_LINE:
        print()
        line_count = 1
print()

print( '편차 제곱 출력 :' )
for i in range( count ):
    print( '{:8.2f}'.format( deviation_squareds[ i ] ), end = '' )
    line_count += 1
    if line_count > MAX_LINE:
        print()
        line_count = 1
print()

print( '\nvariance = {:8.2f}\n'.format( variance ) )
