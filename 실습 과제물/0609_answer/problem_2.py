#
# 2) “홍길동 01012345678 hong@korea.com”을 입력받아 출력 결과와 같이 출력하는 파이썬 스크립트
#
#   [ 출력 결과 ]
# 	이름 : 홍길동
# 	전화번호 : 010 - 1234 - 5678
# 	e-mail : hong@korea.com
#
# 1. 문자열 입력
person = input( "Input person info : " )

# 2. 입력 내용을 이름, 전화번호, e-mail로 분리
person_info = person.split()

# 3. 결과 출력
print( "\n이름 : {}".format( person_info[ 0 ] ) )
print( "전화번호 : {} - {} - {}".format( person_info[ 1 ][ :3 ], person_info[ 1 ][ 3:7 ], person_info[ 1 ][ 7: ] ) )
print( "e-mail : {}".format( person_info[ 2 ] ) )
