#
# 3) 1~10000사이에서 3의 배수와 5의 배수를 한 줄에 10개씩 출력하고,
#   마지막에 3의 배수와 5의 배수 갯수를 출력하는 파이썬 스크립트
#
# symbolic constant
MAX = 10000
MAX_LINE = 10
MULTIPLE3 = 3
MULTIPLE5 = 5

# 1. 변수 정의
count = 0
sum = 0
line_count = 1

# 2. MAX 만큼 반복
for i in range( 1, MAX + 1 ):
    # 2.1 3의 배수와 5의 배수 출력 및 갯수 count
    if ( i % MULTIPLE3 ) == 0 or ( i % MULTIPLE5 ) == 0:
        count += 1
        sum += i
        print( '{:6}'.format( i ), end = '' )
        line_count += 1
        # 2.1.1 한 줄에 10개이면 줄 바꿈
        if ( line_count > MAX_LINE ):
            print()
            line_count = 1

# 3. 결과 출력
print( '\n\n3 multiple or 5 multiple count : {:8}'.format( count ) )
print( '3 multiple or 5 multiple sum : {:10}'.format( sum ) )
