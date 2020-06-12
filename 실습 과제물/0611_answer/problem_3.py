#
# 3) 이름, 전화번호, e-mail을 dict에 저장하고 전체 dict 내용을 출력하며,
#    스크립트 종료시 파일에 dict 내용을 저장하고, 스크립트를 다시 시작하면
#    파일의 내용을 dict에 저장한 후 전체 dict 내용을 출력하는 파이썬 스크립트
# symbolic constant
END = 'end'

# 1. 변수 선언
persons = {}

# 2. 파일로 부터 개인 정보 Load
with open( 'person.txt', 'r' ) as f:
    line = f.readline()
    while line:
        person = line.split()
        persons[ person[ 0 ] ] = person[ 1 ], person[ 2 ]
        line = f.readline()

print( '파일 내용 :' )
for k, v in persons.items():
    print( '{:<20s} {:^15s} {:<30s}'.format( k, v[ 0 ], v[ 1 ] ) )
print()

# 3. 개인 정보 입력( 이름이 end 입력시 입력 종료 )
name = input( 'Input name ( quit : "end" ) : ' )
while name.lower() != END:
    tel = input( 'Input tel : ' )
    email = input( 'Input e-mail : ' )
    persons[ name ] = tel, email
    print()
    name = input( 'Input name ( quit : "end" ) : ' )

# 4. 개인 정보 출력
print()
for k, v in persons.items():
    print( '{:<20s} {:^15s} {:<30s}'.format( k, v[ 0 ], v[ 1 ] ) )

# 5. 개인 정보 파일에 저장
with open( 'person.txt', 'w' ) as f:
    for k, v in persons.items():
        f.write( '{} {} {}\n'.format( k, v[ 0 ], v[ 1 ] ) )
