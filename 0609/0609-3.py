#
# list
#    : 수정 가능한 데이터 집합, 데이터 저장         ->수정 가능다하는 것이 튜플과 가장 큰 차이점
#    : sequence 자료형(순서가 존재한다.)
#    : 인덱싱, 슬라이싱, 결합, 반복, 멤버 검사, 길이 계산의 sequence 자료형
#    : 공통 연산을 적용할 수 있다.
# list 생성
l = [] # 빈 list
print( 'l : {}\tlen( l ) : {}'.format( l, len( l ) ) )

l = [ 1, 2, 'python' ]                     # list는 반드시 대괄호[]가 있어야 함, 콤마만 있으면 튜플 / 자료형이 같이 필요 없음
print( 'l : {}\tlen( l ) : {}'.format( l, len( l ) ) )

colors = [ 'red', ' blue', 'green' ]
print( 'colors : {}\tlen( colors ) : {}'.format( colors, len( colors ) ), '\n' )

# 생섬(변환) 함수 이용한 list 생성
l = list( range( 10 ) )
print( 'l : {}\tlen( l ) : {}'.format( l, len( l ) ) )

l = list( range( 1, 11, 2 ) )           # 1부터 11까지 2단위로
print( 'l : {}\tlen( l ) : {}'.format( l, len( l ) ), '\n' )

# list 내용 포함 확인
print( "red" in colors )
print( "purple" in colors, '\n' )

# list 인덱싱
print( colors[ 0 ] )
print( colors[ 2 ] )
print( colors[ -2 ], '\n' )

# list 슬라이싱
print( colors[ 0:3 ] )
print( colors[ 1:3 ] )
print( colors[ 2: ] )
print( colors[ :2 ] )
print( colors[ ::2 ], '\n' )

# list 결함
print( colors + colors , '\n' )

# list 반복
print( colors * 3, '\n' )

# list 내용 변경
# list 내용 일부 변경
l = [ 'spam', 'eggs', 100, 2020 ]
print( 'l : {}\tlen( l ) : {}'.format( l, len( l ) ) )
l[ 2 ] = l[ 2 ] + 59                                     # l[ 2 ] 의 값에 59를 더한 값을 치환
print( 'l : {}\tlen( l ) : {}'.format( l, len( l ) ), '\n' )

# list 일부 값 치환
l[ 0:2 ] = [ 1, 12 ]
print( 'l : {}\tlen( l ) : {}'.format( l, len( l ) ) )
l[ 0:2 ] = [ 1 ]
print( 'l : {}\tlen( l ) : {}'.format( l, len( l ) ), '\n' )

# list 일부 값 삭제
l = [ 1, 12, 123, 1234 ]
print( 'l : {}\tlen( l ) : {}'.format( l, len( l ) ) )
l[ 0:2 ] = []
print( 'l : {}\tlen( l ) : {}'.format( l, len( l ) ), '\n' )

# list 일부 값 추가
l = [ 123, 1234 ]
print( 'l : {}\tlen( l ) : {}'.format( l, len( l ) ) )
l[ 1:1 ] = [ 'spam', 'ham' ]                               # 1위치에 'spam', 'ham'을 삽입 / 삽입의 기능 * 그냥 insert쓰자
print( 'l : {}\tlen( l ) : {}'.format( l, len( l ) ), '\n' )

# del 명령을 이용한 삭제
del l[ 0 ]
print( 'l : {}\tlen( l ) : {}\n'.format( l, len( l ) ) )

del l[ 1: ]
print( 'l : {}\tlen( l ) : {}\n'.format( l, len( l ) ) )

l = list( range( 4 ) )
print( 'l : {}\tlen( l ) : {}'.format( l, len( l ) ) )
print( 'l : {}\tlen( l ) : {}'.format( l[ ::2 ], len( l ) ) ) # 슬라이싱 한 것을 읽어 온 것일 뿐이지 데이터 자체를 자르지 않음
del l[ ::2 ]
print( 'l : {}\tlen( l ) : {}\n'.format( l, len( l ) ) )      # 데이터 자체를 슬라이싱 한 것

# list 함수
print( 'colors : {}\tlen( colors ) : {}'.format( colors, len( colors ) ) )

colors.append( 'white' )                           # list에 요소를 추가할 때, 추가는 항상 마지막에(오른쪽)
print( 'colors : {}\tlen( colors ) : {}'.format( colors, len( colors ) ) )

colors.extend( [ 'black', 'yellow' ] )
print( 'colors : {}\tlen( colors ) : {}'.format( colors, len( colors ) ) )

colors.insert( 3, 'purple' )
print( 'colors : {}\tlen( colors ) : {}'.format( colors, len( colors ) ) )

colors.insert( 0, 'orange' )
print( 'colors : {}\tlen( colors ) : {}'.format( colors, len( colors ) ), '\n' )

colors.append( 'white' )
print( colors.count( 'white' ) )
print( colors.index( 'white' ), '\n' )

colors.reverse()   # 역순
print( 'colors : {}\tlen( colors ) : {}\n'.format( colors, len( colors ) ) )

colors.sort()      # 정렬 ( 알파벳의 대소비교 -> ASCII코드 값 ), 오름차순(작은것부터)
print( 'colors : {}\tlen( colors ) : {}\n'.format( colors, len( colors ) ) )

colors.sort( reverse= True )
print( 'colors : {}\tlen( colors ) : {}\n'.format( colors, len( colors ) ),'\n' )

l = 'Python is a Programing Language'.split()
print( 'l : {}\tlen( l ) : {}'.format( l, len( l ) ) )
l.sort()
print( 'l : {}\tlen( l ) : {}'.format( l, len( l ) ) )    # 대문자가 앞에 있으니 대문자가 소문자보다 작은 것
l.sort( key= str.lower )                                  # key : value 이기 때문에 키값을 저렇게 주는 것(왼쪽)
print( 'l : {}\tlen( l ) : {}'.format( l, len( l ) ), '\n' )

l = [ 1, 6, 3, 8, 6, 2, 9 ]
print( 'l : {}\tlen( l ) : {}'.format( l, len( l ) ) )
l.sort()                                                  # 메소드 ( l의 내용이 바뀜 ), 원본이 순서가 바뀌어도 가능할 때
print( 'l : {}\tlen( l ) : {}'.format( l, len( l ) ), '\n' )

l = [ 1, 6, 3, 8, 6, 2, 9 ]
new = sorted( l )                                         # 함수 ( l의 내용이 바뀌지 않음 ), 원래 list 순서가 바뀌면 안될때 씀
print( 'l : {}\tlen( l ) : {}'.format( l, len( l ) ) )
print( 'new : {}\tlen( new ) : {}'.format( new, len( new ) ),'\n' )

#(.)다음에 나오는 함수는 메소드(method)함수 라고 함 / (.)없이 호출하면 함수라 호칭
print( 'colors : {}\tlen( colors ) : {}'.format( colors, len( colors ) ) )
colors.remove( 'red' )
print( 'colors : {}\tlen( colors ) : {}'.format( colors, len( colors ) ) )

del colors[ : ]
print( 'colors : {}\tlen( colors ) : {}\n'.format( colors, len( colors ) ),'\n' )

l = []
l.append( 5 )
l.append( 10 )
l.append( 15 )
print( 'l : {}\tlen( l ) : {}\n'.format( l, len( l ) ) )
print( l.pop() )      # append는 항상 끝에다 추가를 하지만, append를 한 마지막(오른쪽부터) 끄집어 내서 삭제함
print( 'l : {}\tlen( l ) : {}'.format( l, len( l ) ) )
print( l.pop() )
print( 'l : {}\tlen( l ) : {}'.format( l, len( l ) ) )
print( l.pop() )
print( 'l : {}\tlen( l ) : {}'.format( l, len( l ) ),'\n' )
# -> pop을 할때마다 오른쪽 데이터부터 끄집어서 삭제함

# 중첩 list (2차원)
korScore = [ 59, 99, 79 ]
engScore = [ 57, 97, 77 ]
midterm = [ korScore, engScore ]
print( 'midterm : {}\nlen( midterm ) : {}'.format( midterm, len( midterm ) ) )

print( '\n', midterm[ 0 ] )
print( midterm[ 0 ][ 1 ] )
print( midterm[ 0 ][ 1: ],'\n' )

# list의 패킹/언패킹
t = [ 1, 2, 3 ]        # 패킹
a, b, c = t            # 언패킹
print( t )
print( a, b, c )


























































