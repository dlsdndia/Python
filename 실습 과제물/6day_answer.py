#!/usr/bin/env python
# coding: utf-8

# # 미국 대통령 평균 신장은 얼마일까?

# ## 0. NumPy import

import numpy as np


# ## 1. 파일 내용 저장 파이썬 리스트 변수 선언
order_list = []
name_list = []
height_list = []


# ## 2. 파일에 데이터 읽기( president_heights.csv )
with open( 'president_heights.csv', 'r' ) as f:
    line = f.readline() # 제목줄 제거
    line = f.readline()
    while line:
        data = line.split( ',' )
        order_list.append( data[ 0 ] )
        name_list.append( data[ 1 ] )
        height_list.append( int( data[ 2 ][ : 3 ] ) ) # 키 마지막 줄바꿈( \n ) 제거
        line = f.readline()


# ## 3. 읽은 데이터 확인( 처음 5개, 마지막 5개 )
print( order_list[ :5 ], order_list[ len( order_list ) - 5 : ], '\n' )
print( name_list[ :5 ], name_list[ len( name_list ) - 5 : ], '\n' )
print( height_list[ :5 ], height_list[ len( height_list ) - 5: ], '\n' )

# ## 4. NumPy 배열 생성
# ### 4.1 전체 대통령 순번
order_array = np.array( order_list )
print( order_array )
print( order_array.ndim, order_array.shape, order_array.size, order_array.dtype, '\n' )

# ### 4.2 전체 대통령 이름
name_array = np.array( name_list )
print( name_array )
print( name_array.ndim, name_array.shape, name_array.size, name_array.dtype, '\n' )

# ### 4.3 전체 대통령 신장
height_array = np.array( height_list )
print( height_array )
print( height_array.ndim, height_array.shape, height_array.size, height_array.dtype, '\n' )


# ## 5. 데이터에 대한 통계 / 집계 출력
print( '평균 신장             : {:6.2f}'.format( height_array.mean() ) ) # 평균 신장
print( '신장에 대한 표준편차  : {:6.2f}'.format( height_array.std() ) ) # 신장에 대한 표준 편차
print( '최소 신장 대통령 정보 : {:3d}( {:>2s} {:<22s})'.format( height_array.min(), 
                                                                order_array[ height_array.argmin() ],
                                                                name_array[ height_array.argmin() ] ) ) # 최소 신장 대통령 정보
print( '최고 신장 대통령 정보 : {:3d}( {:>2s} {:<22s})'.format( height_array.max(), 
                                                                order_array[ height_array.argmax() ],
                                                                name_array[ height_array.argmax() ] ) ) # 최고 신장 대통령 정보

print( "신장에 대한 1사분위수 : {:6.2f}".format( np.percentile( height_array, 25 ) ) )
print( "신장에 대한 중앙값    : {:6.2f}".format( np.median( height_array ) ) )
print( "신장에 대한 3사분위수 : {:6.2f}".format( np.percentile( height_array, 75 ) ) )
