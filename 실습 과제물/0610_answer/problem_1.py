#
# 1) 1~100까지의 짝수 합과 홀수 합을 출력하는 파이썬 스크립트
#
# symbolic constant
MAX = 100

# 1. 변수 정의
even_sum = odd_sum = 0

# 2. MAX만큼 반복
for i in range( MAX + 1 ):
    # 2.1 짝수 합과 홀수 합 계산
    if ( i % 2 ) == 0:
        even_sum += i
    else:
        odd_sum += i

# 3. 결과 출력
print( '방법 하나'.center( 30, '-' ) )
print( 'Even sum : {:5d}\tOdd sum : {:5d}\n'.format( even_sum, odd_sum ) )

# 1. 변수 정의
even_sum = odd_sum = 0

# 2. 홀수 합 계산
for i in range( 1, MAX + 1, 2 ):
    odd_sum += i

# 3. 짝수 합 계산
for i in range( 2, MAX + 1, 2 ):
    even_sum += i

# 4. 결과 출력
print( '방법 또하나'.center( 30, '-' ) )
print( 'Even sum : {:5d}\tOdd sum : {:5d}\n'.format( even_sum, odd_sum ) )
