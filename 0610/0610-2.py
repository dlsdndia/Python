#
# set ( 집합 )
#   : 순서 없이 중복 없이 저장하는 set 자료형 (중복되느 값이 있으면 하나만 씀), 순서가 없다는 것은 순서 신경 쓰지 않는 다는 것
#   : 변경 가능한 자료형
#   : 집합연산 할 때 쓰는 자료형
#
# set 생성
s = set()
print( "s : {}( {} )".format( s, len( s ) ) )
s = set( [ 1, 2, 3, 1, 2, 3 ] )
print( "s : {}( {} )".format( s, len( s ) ) )
s = { 1, 2, 3, 1, 2, 3 }
print( "s : {}( {} )\n".format( s, len( s ) ) )

s = set( ( 1, 2, 3, 1, 2, 3 ) )                    # tuple 이용 set 생성
print( "s : {}( {} )".format( s, len( s ) ) )
s = set( 'hello' )                                 # str(문자열) 이용 set 생성
print( "s : {}( {} )".format( s, len( s ) ) )
s = set( [ 1, 2, 3 ] )                             # list 이용 set 생성
print( "s : {}( {} )".format( s, len( s ) ) )
s = set( { 'one':1, 'two':2 } )                    # dict 이용 set 생성
print( "s : {}( {} )".format( s, len( s ) ) )

l1 = [ 1, 2, 3 ]
l2 = [ 3, 4, 5 ]
# s = { l1, l2 }                                   # set의 원소에는 변경 불가능한 자료형만 가능( list값은 변경 가능하지만,
                                                   # list 자체를 가져왔으므로 list는 변경 가능해서 에러가 남)
print( "s : {}( {} )".format( s, len( s ) ) )

# set 함수(연산, 메소드)
s = { 1, 2, 3, 1, 2, 3 }
print( "s : {}( {} )\n".format( s, len( s ) ) )

s.add( 1 )                                       # 원소 추가
print( "s : {}( {} )".format( s, len( s ) ) )
s.add( 5 )
print( "s : {}( {} )\n".format( s, len( s ) ) )

s.remove( 1 )                                    # 원소 삭제
print( "s : {}( {} )\n".format( s, len( s ) ) )

s.update( [ 1, 4, 5, 6, 7 ] )                    # 해당 set에 대한 합집합 (해당 하는 데이터를 합한다)
print( "s : {}( {} )\n".format( s, len( s ) ) )

s.discard( 3 )                                   # 해당 원소 제거, 해당 원소가 없으면 무시
print( "s : {}( {} )".format( s, len( s ) ) )
s.discard( 3 )                                   # 삭제할게 없으면 그냥 넘어 감
print( "s : {}( {} )\n".format( s, len( s ) ) )

# s.remove( 3 )                                    # 해당 원소 제거, 해당 원소가 없으면 예외 발생(처리동작이 안됨)
# print( "s : {}( {} )\n".format( s, len( s ) ) )
# discard 는 삭제할 것이 없어도 그냥 넘어가지만 remove는 원소가 없으면 에러**

s.clear()
print( "s : {}( {} )\n".format( s, len( s ) ) )

# set 집합 연산
s1 = { 1, 2, 3, 4, 5 }
s2 = { 3, 4, 5, 6, 7 }

print( "합집합" )               # 중복을 허용하지않고 합함
print( s1.union( s2 ) )
print( s1 | s2, '\n' )

print( "교집합" )               #
print( s1.intersection( s2 ) )
print( s1 & s2, '\n' )

print( "차집합" )               # 집합s1에서 s2것을 빼는 것 s1에서 남는 것만 보여줌
print( s1.difference( s2 ) )
print( s1 - s2, '\n' )
# www.python.org 에 들어가서 도큐먼츠 카테고리에 들어가서 밑에 리소스 -> 튜토리얼 또는 라이브러리 레퍼런스에서 검색하면 자세한 설명나옴



























