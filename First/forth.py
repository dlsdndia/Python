#표준 입/줄력
result = None

number1 = int( input( "Input number1 : " ) )   # input = 입력 함수, input()가로 안에는 화면에 출력되는 것, 꼭 정수로 형변환 해야함
number2 = int( input( "Input number2 : " ) )

result = number1 + number2

print( number1, '\t', number2, '\t', result )              # 탭간격으로 출력한 것, 숫자에 자리수가 다르면 모양이 매번 달라짐
print( '%5d + %5d = %10d' % ( number1, number2, result ) ) # 5d는 전체 5자리로 만들고 거기에 숫자를 출력 하라는 것,
                                                             # 10d는 10자리를 확보하고 숫자를 출력하란는 것
                                                             # %[전체자리수]d : d(decima number)는 출력 형식
                                                             # 지금 이 방식은 python2에서 쓰는 방식
print( '{0:5} + {1:5} = {2:10}'.format( number1, number2, result ) ) # python3에서 사용하는 방식 3.0버전 이상
# 0이면 1번째 변수, 1이면 두번째 변수, 2는 3번째 변수(result)
# :숫자에서 숫자는 자릿수














