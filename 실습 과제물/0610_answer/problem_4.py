#
# 4) -99999가 입력될 때까지 정수를 입력받아 평균, 편차, 편차제곱, 분산을
#    출력하는 파이썬 스크립트
#
# symbolic constant
END = -99999
MAX_LINE = 10

# 1. 변수 정의
numbers = []
total = 0
deviations = []
deviation_squareds = []
deviation_squareds_total = 0

# 2. END가 입력될 때 까지 반복하며 저장
i = 1
number = int( input( "Input number[ %5d ] : " % ( i ) ) ) # 파이썬2버전 형식
while number != END:
    numbers.append( number )
    total += number
    i += 1
    number = int(input("Input number[ %5d ] : " % ( i ) ) )

count = len( numbers )

# 3. 평균 계산
mean = total / count

# 4. 편차, 편차 제곱 계산
for i in range( count ):
    deviations.append( numbers[ i ] - mean )
    deviation_squareds.append( deviations[ i ] ** 2 )
    deviation_squareds_total += deviation_squareds[ i ]

# 5. 분산 계산
variance = deviation_squareds_total / count

# 6. 결과 출력
print()
line_count = 1
for i in range( count ):
    print( '{:8}'.format( numbers[ i ] ), end = '' )
    line_count += 1
    if line_count > MAX_LINE:
        print()
        line_count = 1
print()

print( '\nmean = {:8.2f}\n'.format( mean ) )

for i in range( count ):
    print( '{:8.2f}'.format( deviations[ i ] ), end = '' )
    line_count += 1
    if line_count > MAX_LINE:
        print()
        line_count = 1
print()

for i in range( count ):
    print( '{:8.2f}'.format( deviation_squareds[ i ] ), end = '' )
    line_count += 1
    if line_count > MAX_LINE:
        print()
        line_count = 1
print()

print( '\nvariance = {:8.2f}\n'.format( variance ) )

