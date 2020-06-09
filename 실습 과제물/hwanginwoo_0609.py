# hwanginwoo_06/09

# 1) “홍길동01012345678”을 문자열 변수에 저장 후 출력 결과와 같이 출력하는 파이썬 스크립트
data = "홍길동01012345678"
print( data[ 0:3 ] + "(",data[ 3:6 ], "-", data[ 6:10 ], "-", data[ 10: ], ")" )

# 2) “홍길동 01012345678 hong@korea.com”을 입력받아 출력 결과와 같이 출력하는 파이썬 스크립트
data = "홍길동 01012345678 hong@korea.com "
print( "이름 : {}".format( data[ 0:3 ] ) )
print( "전화번호 : {}".format( data[ 3:7 ] + "-" + data[ 7:11 ] + "-" + data[ 11:15 ] ) )
print( "e-mail : {}".format( data[ 16: ] ) )
# 3) 두 정수를 입력 받아 합계, 평균을 출력하는 파이썬 스크립트( list 이용 )
count = 0
number1 = int( input( " input number1 : " ) )
count += 1
number2 = int( input( " input number2 : " ) )
count += 1
number = [ number1, number2 ]
print( "합계 : {}".format(number[0] + number[1] ) )
print( "평균 : {}".format(number[0] + number[1] / count ) )

# 4) 다섯 정수를 입력받아 평균, 편차, 편차제곱, 분산을 출력하는 파이썬 스크립트( list 이용 )
number1 = int( input( " input number1 : " ) )
number2 = int( input( " input number2 : " ) )
number3 = int( input( " input number3 : " ) )
number4 = int( input( " input number4 : " ) )
number5 = int( input( " input number5 : " ) )
number = [ number1, number2, number3, number4, number5 ]
print( "합계 : {}".format(number[0] + number[1] + number[2] + number[3] + number[4] ) )
print( "평균 : {}".format(number[0] + number[1] + number[2] + number[3] + number[4] / 5 ) )

# 5) 3명 학생의 이름, 과목1 점수, 과목2 점수, 과목3 점수를 입력받아 출력 결과와 같이 출력하는 파이썬 스크립트( list 이용 )

student1 = input( " input  1name : " ) + input( " input  score1 : " ) + input( " input  score2 : " ) + input( " input  score3 : " )
student2 = input( " input  2name : " ) + input( " input  score1 : " ) + input( " input  score2 : " ) + input( " input  score3 : " )
student3 = input( " input  3name : " ) + input( " input  score1 : " ) + input( " input  score2 : " ) + input( " input  score3 : " )
student = [ student1, student2, student3 ]
print( "{}\n{}\n{}".format(student[0][0:4]+student[0][4:6]+student[0][6:8]+student[0][8:],
                           student[1][0:4]+student[1][4:6]+student[1][6:8]+student[1][8:],
                           student[2][0:4]+student[2][4:6]+student[2][6:8]+student[2][8:] ) )


