#
# 5) 3명 학생의 이름, 과목1 점수, 과목2 점수, 과목3 점수를 입력받아 출력 결과와 같이 출력하는 파이썬 스크립트( list 이용 )
#
#   [ 출력 결과 ]
# 	hong	50	50	50	150	50.00
# 	kim		90	90	90	270	90.00
# 	lee		70 	70	70 	210	70.00
#
# 0. 과목수 상수와 3명 학생 저장 list 생성
SUBJECT_MAX = 3             # 대문자로 쓰면 상수라는 표현, 상수는 바뀌지 않는다.

students = []

# 1. 3명 학생 정보 입력
# 1.1 첫번째 학생 정보 입력
student = []
name = input( "Input name : " )
student.append( name )

subject = int( input( "Input subject1 : " ) )
student.append( subject )

subject = int( input( "Input subject2 : " ) )
student.append( subject )

subject = int( input( "Input subject3 : " ) )
student.append( subject )
students.append( student )

# 1.2 두번째 학생 정보 입력
student = []
name = input( "\nInput name : " )
student.append( name )

subject = int( input( "Input subject1 : " ) )
student.append( subject )

subject = int( input( "Input subject2 : " ) )
student.append( subject )

subject = int( input( "Input subject3 : " ) )
student.append( subject )
students.append( student )

# 1.3 세번째 학생 정보 입력
student = []
name = input( "\nInput name : " )
student.append( name )

subject = int( input( "Input subject1 : " ) )
student.append( subject )

subject = int( input( "Input subject2 : " ) )
student.append( subject )

subject = int( input( "Input subject3 : " ) )
student.append( subject )
students.append( student )

# 2. 학생별 총점/평균 계산
sum = students[ 0 ][ 1 ] + students[ 0 ][ 2 ] + students[ 0 ][ 3 ]
mean = sum / SUBJECT_MAX
students[ 0 ].append( sum )
students[ 0 ].append( mean )

sum = students[ 1 ][ 1 ] + students[ 1 ][ 2 ] + students[ 1 ][ 3 ]
mean = sum / SUBJECT_MAX
students[ 1 ].append( sum )
students[ 1 ].append( mean )

sum = students[ 2 ][ 1 ] + students[ 2 ][ 2 ] + students[ 2 ][ 3 ]
mean = sum / SUBJECT_MAX
students[ 2 ].append( sum )
students[ 2 ].append( mean )

# 3. 결과 출력
print( '\n{:<20s}\t{:3d}\t{:3d}\t{:3d}\t{:5d}\t{:6.2f}'.format( students[ 0 ][ 0 ],
                                                                students[ 0 ][ 1 ],
                                                                students[ 0 ][ 2 ],
                                                                students[ 0 ][ 3 ],
                                                                students[ 0 ][ 4 ],
                                                                students[ 0 ][ 5 ] ) )
print( '{:<20s}\t{:3d}\t{:3d}\t{:3d}\t{:5d}\t{:6.2f}'.format( students[ 1 ][ 0 ],
                                                              students[ 1 ][ 1 ],
                                                              students[ 1 ][ 2 ],
                                                              students[ 1 ][ 3 ],
                                                              students[ 1 ][ 4 ],
                                                              students[ 1 ][ 5 ] ) )
print( '{:<20s}\t{:3d}\t{:3d}\t{:3d}\t{:5d}\t{:6.2f}'.format( students[ 2 ][ 0 ],
                                                              students[ 2 ][ 1 ],
                                                              students[ 2 ][ 2 ],
                                                              students[ 2 ][ 3 ],
                                                              students[ 2 ][ 4 ],
                                                              students[ 2 ][ 5 ] ) )
