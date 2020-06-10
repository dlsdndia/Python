#
# 제어 구조
#   : 프로그램의 실행 구조를 결정
#     1. 순차구조 : 위에서 아래로 차례대로 명령을 실행 하는 구조
#     2. 선택구조 : 조건 판단의 결과에 따라 실행 방향을 결정하는 구조 (비교하는 구조)
#     3. 반복구조 : 정해진 횟수나 조건에 따라 일정한 명령 집합( 코드 블록 )을 반복해서 실행하는 구조
#
#   프로그램을 자료형, 연산자, 제어문을 활용하여 문제에서 요구하는 사항을 해결하는 명령 집합( 코드 블록 )이다
#
# 선택구조( if ~ elif ~ else )
#  if < 조건식1 >:
#      < 명령문1 >     -> 조건식1이 참일 때 수행
#  [elif < 조건식2 >:]
#         < 명령문2 >  -> 조건식2가 참일 때 수행
#   [else:]
#         < 명령문3 >  -> 모든 조건이 만족하지 않을 때
#
# 선택 구조 형태
# 1. 단순 선택 구조 -> if만 사용
# 2. 양자 택일 구조 -> if ~ else
# 3. 다중 선택 구조 -> if ~ [elif ...(여런번 가능 ).... ]~ else
#
number = 10
if number > 0:                # 조건식  (선택 구조 - 단순 선택 )
    print( "Yes, sir!!!\n" )  # 명령문

if number != 0 and number > 0:
    print( "Yes, sir!!!" )                      # 인덴테이션이 밑이랑 같기 때문에 밑에와 같이 참이면 두개다 실행
    print( "number : {}\n".format( number ) )   # 인덴테이션( 위랑 간격 )이 위랑 같기 때문에 참이면 같이 실행

number = -10
if number != 0 and number > 0:
    print( "Yes, sir!!!" )
print( "number : {}\n".format( number ) )    # 참이든 거짓이든 무조건 실행 (인덴테이션(줄간격)이 같지 않음)

# 다중 선택
if number != 0 and number > 0:
    print( "Positive" )
elif number != 0 and number < 0:
    print( "Negative" )
else:
    print( "zero" )
print( "number : {}\n".format( number ) )

order = 'spagetti'
if order == 'spam':
    price = 500
elif order == 'ham':
    price = 700
elif order == 'egg':
    price = 100
elif order == 'spagetti':
    price = 1000
else:
    price = 0
print( "order : {}\tprice : {}\n".format( order, price ) )

# 2. 양자 택일 구조
lunch = '먹는다'
if lunch == '먹는다':
    print( "살찌겠군!!!\n" )
else:
    print( "몸 망가지겠군!!!\n" )

# 선택구조 대신에 dict를 사용하는 것이 더 편리할 때도 있다.
# 이 형태가 가장 Python 스러운 code
order = 'spam'
menu = { 'spam':500, 'ham':700, 'egg':100, 'spagetti':1000 }
price = menu.get( order, 0 )       # 해당하는 key로 원하는 값을 가져오는 것 ,0은 없으면 0 을 가져오라는 것
print( "Order : {}\tprice : {}\n".format( order, price ) )

# 삼항 연산자를 이용한 선택
if price >= 500:
    message = "VIP"
else:
    message = "non VIP"
print( "Order : {}\tprice : {}\t{}\n".format( order, price, message ) )

# 삼항 연산자 (양자 택일 일때만 씀)-> if ~ else 만 쓰일 때
# python스러운 간결한 코드 코드 길이가 짧음(위아래로)
#          참       조건             거짓
message = "VIP" if price >= 500 else "non VIP"  #  -> message에 if면 vip치환하고 else면 non치환해라 라는 것
print( "Order : {}\tprice : {}\t{}\n".format( order, price, message ) )

































