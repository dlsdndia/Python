#
# 함수
#   : 단위 기능(하나의 기능)을 수행하는 코드 집합(코드 블럭), 중복되는 처리를 수행하는 코드 블록을 별도로 작성한 후 필요시 호출해서 사용한다.
#
# 함수 사용을 통해 얻을 수 있는 점
#  1. 중복 코드 방지를 통한 유지 보수성 향상
#  2. 특정 기능에 대하여 별도로 구현하지 않고 호출하여 사용
#  3. 팀 작업을 수행할 때 팀원들은 함수 중심으로 작성하여 차후 통합을 수월하게 할 수 있다.
#
# 함수는 함수 정의, 함수 호출 두 부분으로 구성되어 있으며
# 파이썬에서는 반드시 함수 정의가 함수 호출보다 먼저 수행되어야 한다.
#
# 객체에 소속된 함수는 메서드(method)라고 부른다.
#
# 함수 정의 형식
# def < 함수이름 >( [ 인수 목록 ] ):             -> 인수는 생략 가능하다 즉 [ 인수 목록 ] 은 생략 가능 그치만 그걸 감싸는 ()생략x
#  함수 내용
#  [ return < 값 > ]
#
# 함수 유형
# 1. 인수 없고, return 값 없는 유형
def myPrint():
    print( 'Welcome Python world!!!' )

# 2. 인수 없고, return 값 있는 유형          # 비교적 없음
def myPrint2():
    print( 'Welcome Python world!!!' )
    return True
# 3. 인수 있고, return 값 없는 유형
def myAdd( number1, number2 ):
    result = number1 + number2
    print( '{} + {} = {}'.format( number1, number2, result ) )
# 4. 인수 있고, return 값 있는 유형
def myAdd2( number1, number2 ):
    result = number1 + number2
    return result

# 함수 호출
myPrint()
myPrint2()
print( myPrint2 )
myAdd( 10, 5 )
print( '{} + {} = {}'.format( 10, 5, myAdd2( 10, 5 ) ) ) # 항상 출력하지 않고 값만 만드는 경우 myAdd2가 났다. 목적에 따라 다름

#
# 함수의 return값을 한 개만 가능하다
#
def calculate( number1, number2 ):
    add = number1 + number2
    subtract = number1 - number2
    multiple = number1 * number2
    divide = number1 / number2
    remainder = number1 % number2

    return add, subtract,multiple, divide, remainder

number1, number2 = 10, 5
result = calculate( number1, number2 )
print( '{:3d} + {:3d} = {:5d}'.format( number1, number2, result[0] ) )
print( '{:3d} - {:3d} = {:5d}'.format( number1, number2, result[1] ) )
print( '{:3d} * {:3d} = {:5d}'.format( number1, number2, result[2] ) )
print( '{:3d} / {:3d} = {:5.2f}'.format( number1, number2, result[3] ) )
print( '{:3d} % {:3d} = {:5d}'.format( number1, number2, result[4] ) )

#
# 문) 값을 입력 받아 합계를 return하는 함수
#
# 함수 정의
def mySum( numbers ):
# 1. 합계 저장하는 변수 생성, 0으로 초기화
    sum = 0
# 2. 인수( numbers )만큼 반복
    for value in numbers:
#   2.1 합계 저장 변수에 numbers의 내용 하나를 누적
        sum += value
# 3. 합계 return
    return sum

#
# 문) 인수를 전달받아 최고값을 return하는 함수
#
def myMax( numbers ):
# 1. 최고값 저장 변수 생성
    max = numbers[0]
# 2. 인수 길이만큼 반복
    for value in numbers:
#  2.1 최고값 파악
        if max < value:
            max = value
# 3. 최고값 return
    return max

# 문) 인수를 전달받아 최저값을 return하는 함수
def myMin( numbers ):
    min = numbers [ 0 ]
    for value in numbers:
        if min > value:
            min = value
    return min

#
# 문) 인수를 전달받아 평균을 return하는 함수
def myMean( numbers ):
    return mySum( numbers ) / len( numbers )

# 문) 인수를 전달받아 최대값과 최소값을 return하는 함수
def myMaxAndMean( numbers, mean ):
    return tuple ( [ value - mean for value in numbers ] )

# 문) 인수를 전달받아 편차를 return하는 함수
def myDeviation( numbers ):
    return tuple([value ** 2 for value in numbers])

# 문) 인수를 전달받아 편차 제곱을 return하는 함수
def myDeviationsequared( numbers ):

# 문) 인수를 전달받아 분산값을 return하는 함수
def myVariance( numbers ):
    count = len( numbers )
    mean = myMean( numbers )
    deviation = [ value - mean for value in numbers ]
    deviation_squareds = [ value ** 2 for value in deviation ]
    variance = mySum( deviation_squareds ) / count
    return variance

#
# 문) 다음과 같이 출력되는 mySummary() 정의
#       변량 :
#       최대값 :
#       최소값 :
#       평균값 :
#       편차 :
#       분산 :
#
def mySummary():
    print( '변량' )
    line_count = 1
    for value in numbers:
        print( '{:8d}'.format( value ) )
        line_count += 1
        if line_count > 10:
            line_count = 1; print()
    print( '최댓값 : {}'.format( myMax( numbers ) ) )
    print( '최솟값 : {}'.format( myMin( numbers ) ) )
    mean - myMean( numbers )
    print( '평균값 : {:.2f}'.format( mean ) )
    print( '편차 : ' )
    line_count = 1
    for value in myDeviation( numbers, mean ):
        print( '{:8d}'.format( value ) )
        line_count += 1
        if line_count > 10:
            line_count = 1; print()
    print( '분산 : {:.2f}'.format( myVariance( numbers ) ) )

if __name__== ' __main__':                   # 이름이  __main__일때만 실행해라
# 현재 모듈을 단독으로 실행할 때 __name__이 '__name__'이 된다.
# 이와 같은 조건을 부여하면 import 할 때는 실행 되지 않고, 단독으로 모듈을 실행할 때만 동작한다.
# 함수 호출
numbers = [ 5, 3, 1, 4, 2 ]
sum = mySum( numbers )
print( 'sum : {}'.format( sum ) )
print( 'max : {}'.format( myMax( numbers ) ) )
print( 'min : {}'.format( myMin( numbers ) ) )
print( 'mean : {}'.format( myMean( numbers ) ) )
print( myMaxAndMean( numbers ) )
print( 'variance : {}'.format( myVariance( [ 177, 175, 179, 181, 183 ] ) ) )
mySummary( [ 177, 175, 179, 181, 183 ] )














