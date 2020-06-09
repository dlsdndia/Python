# 1. 두 정수를 입력 받아 합계, 평균을 출력하는 파이썬 스크리브
number1 = int( input( "Input number1 : " ) )
number2 = int( input( "Input number2 : " ) )

number3 = number1 + number2
print(number3)
number = [ number1, number2 ]
number_sum = 0
subject_num = 0
for score in number:
    number_sum = number_sum + score
    subject_num = subject_num + 1

average = number_sum / subject_num
print( "총점:{0}, 평균:{1}".format( number_sum, average ) )


# 2. 다섯 정수를 입력받아 평균, 편차, 편차제곱, 분산을 출력하는 파이썬 스크립트
number4 = int( input( "Input number1 : " ) )
number5 = int( input( "Input number2 : " ) )
number6 = int( input( "Input number1 : " ) )
number7 = int( input( "Input number2 : " ) )
number8 = int( input( "Input number1 : " ) )
number9 = int( input( "Input number2 : " ) )