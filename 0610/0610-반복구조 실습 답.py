# 1. 정수 5개를 list에 기억시킨 후 가장 큰 수와 가장 작은수를
#    출력하는 파이썬 스크립트

l = [ 1, 3, 4, 5, 2 ]
print( 'l = {}( {} )\n'.format( l, len( l ) ) )
max = min = l[0]
for i in range( 1, len( l ) ):
    if max < l[ i ]:
        max = l[ i ]

    if min > l[ i ]:
        min = l[ i ]
print( 'max = {}\tmin = {}'.format( max, min ) )


print()
l = [ 1, 3, 4, 5, 2 ]
max = min = l[0]
for i in range( 1, len( l ) ):
    if max < l[ i ]:
        max = l[ i ]

    if min > l[ i ]:
        min = l[ i ]
print( 'max = {}\tmin = {}'.format( max, min ) )















