#
# 2) 20개의 정수를 입력 받아 양수/음수의 개수, 양수일 때 짝수/홀수 개수를
#    출력하는 파이썬 스크립트
#
# symbolic constant
MAX = 20

# 1. 변수 정의
positive = negative = even = odd = error = 0

# 2. MAX 만큼 반복
for i in range( 1, MAX + 1 ):
    # 2.1 입력
    number = int( input( 'Input [ %2d ] number : ' % ( i ) ) )

    # 2.2 0이 아니면 양수/음수 판별, 짝수/홀수 판별
    if number != 0:
        if number > 0:
            positive += 1
            if ( number % 2 ) == 0:
                even += 1
            else:
                odd += 1
        else:
            negative += 1
    else:
        error += 1
        print('Error data'.center( 30, '-' ) )

# 3. 결과 출력
print( '\npositive count : {:5d}'.format( positive ) )
print( '\teven count : {:5d}\n\t odd count : {:5d}'.format( even, odd ) )
print( 'negative count : {:5d}\n'.format( negative ) )
print( 'error count : {:5d}'.format( error ) )
