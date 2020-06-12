#
#  list comprehension 기능을 이용하여 2단~9단을 list에 저장한 후 출력 결과와 같이 출력하는 파이썬 스크립트
#
# 	[ 출력 결과 ]
# 	2 x 1 = 2
# 	2 x 2 = 4
# 	     ...
# 	2 x 9 = 18
#
# 	      ...
# 	9 x 8 = 72
# 	9 x 9 = 81
# 1. 구구단표 list 생성
multiples = [ [ ( i, j, i * j ) for i in range( 2, 10 ) ] for j in range( 1, 10 ) ]

# 2. 구구단표 출력
for j in range( 8 ):
    for i in range( len( multiples ) ):
        print( '{:2d} X {:2d} = {:2d}'.format( multiples[ i ][ j ][ 0 ],
                                               multiples[ i ][ j ][ 1 ],
                                               multiples[ i ][ j ][ 2 ] ) )
    print()
