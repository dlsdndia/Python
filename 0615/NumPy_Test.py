#!/usr/bin/env python
# coding: utf-8

# # NumPy( Numerical Python )

# ## https://numpy.org

# - 조밀한 데이터 버퍼에서 저장하고 처리하는 효과적인 인터페이스를 제공
# - NumPy 배열은 파이썬의 내장 타입인 list와 비슷하지만 배열의 규모가 커질수록 데이터 저장 및 처리에 훨씬 더 효율적이다.
# - NumPy 배열은 파이썬의 데이터 과학 도구로 구성된 전체 생태계의 핵심을 이루고 있다.

# - 파이썬 데이터 과학 도구 생태계
#     - NumPy : 배열 표현
#     - Pandas : 데이터 처리
#     - Matplotlib : 시각화 처리

# #### NumPy를 사용하기 위해서는 import문을 통해 numpy를 import 한다.

# In[1]:


import numpy as np


# In[2]:


np.__version__


# ## NumPy 배열과 파이썬 배열의 비교

# #### 파이썬은 데이터를 효율적이 고정 타입 데이터 버퍼에 저장하는 다양한 방식을 제공
# #### 내장 array 모듈은 단일 타입의 조밀한 배열( dense array )을 만드는데 사용할 수 있다.

# In[3]:


import array


# In[4]:


L = list( range( 10 ) )
a = array.array( 'i', L )
a


# - array는 기존의 list보다 동일 자료형을 저장하는 배열이므로 속도가 빠르다.
# - array보다 더 유용한 배열은 NumPy 모듈의 ndarray 객체이다.
# - 파이썬의 array 객체는 배열 기반의 데이터에 효율적인 저장소를 제공하는 반면, NumPy는 그 데이터의 효율적인 연산을 추가한다.

# #### NumPy를 이용한 배열 생성

# In[5]:


np.array( [ 1, 4, 2, 5, 3 ] )


# - 파이썬 리스트와 달리 NumPy는 배열의 모든 요소가 같은 타입이어야 한다.
# - 타입이 일치하지 않으면 NumPy는 가능한 경우 상위 타입으로 변환하여 저장한다.

# In[6]:


np.array( [ 3.14, 4, 2.3 ] )


# - 파이썬 list는 다양한 자료형을 저장하는 배열( import 없이 사용 )
# - 파이썬 array는 동일한 자료형을 저장하는 배열( import array 필요 )
# - NumPy ndarray는 동일한 자료형을 저장하는 배열( 배열에 대한 연산이 포함 )   
#   ( import numpy as np 필요 )

# ## NumPy 배열을 생성하는 다양한 방법

# ###  https://numpy.org/doc/stable/user/basics.creation.html

# - 규모가 큰 배열의 경우 NumPy에 내장된 함수를 사용하여 처음부터 배열을 생성하는 것이 더 효율적이다.

# - 기본 1차원 배열 생성 ( 열의 집합 )

# In[7]:


np.array( [ 1, 2, 3, 4, 5 ] )


# - 기본 2차원 배열 생성 ( 행/열의 집합 )

# In[8]:


np.array( [ range( i, i + 3 ) for i in [ 2, 4, 6 ] ] )


# In[9]:


np.array( [ [ 2, 3, 4 ],
            [ 4, 5, 6 ],
            [ 6, 7, 8 ] ] )


# #### 0으로 채운 길이 10의 정수 배열 생성

# In[10]:


np.zeros( 10, dtype = int )


# 1로 채운 3 X 5 부동 소수점 배열 생성

# In[11]:


np.ones( ( 3, 5 ), dtype = float )


# #### 3.14로 채운 3 X 5 배열 생성

# In[12]:


np.full( ( 3, 5 ), 3.14 )


# #### 선형 수열로 채운 배열 생성

# In[13]:


# 0에서 시작해서 2씩 더해 20까지 채움( 내장 함수 range()와 유사 )
np.arange( 0, 20, 2 )


# #### 0과 1사이에 일정한 간격을 가진 다섯 개의 값을 채운 배열 생성

# In[14]:


np.linspace( 0, 1, 5 )


# #### 균등하게 분포된 3 X 3 배열 생성( 0 ~ 1 사이의 난수로 채움 )

# In[15]:


np.random.random( ( 3, 3 ))


# #### 정규 분포( 평균 = 0, 표준편차 = 1 )의 난수로 채운 3 X 3 배열 생성

# In[16]:


np.random.normal( 0, 1, ( 3, 3 ) )


# #### [ 0, 10 ] 구간의 임의의 정수를 채운 3 X 3 배열 생성

# In[17]:


np.random.randint( 0, 10, ( 3, 3 ) )


# #### 3 X 3 크기의 단위 행렬 생성

# In[18]:


np.eye( 3 )


# #### 세 개의 정수를 가지는 초기화 되지 않은 배열 생성, 초기화 되는 값은 해당 메모리 위치에 이미 존재하고 있는 값( gabage 값 )으로 채운다.

# In[19]:


np.empty( 3 )


# ## NumPy 표준 데이터 타입

# ### https://numpy.org/doc/stable/user/basics.types.html

# #### NumPy 배열은 한 가지 타입의 값을 담고 있으므로 해당 타입과 그 타입의 제약 사항을 자세히 알고 사용하는 것이 중요하다.

# #### 배열을 구성할 때 데이터 타입은 문자열을 이용해 지정

# In[20]:


np.zeros( 10, dtype = 'int16' )


# #### 해당 데이터 타입과 관련된 NumPy 객체를 사용해 지정

# In[21]:


np.zeros( 10, dtype = np.int16 )


# ## NumPy 배열 사용

# - 파이썬에서 데이터 처리는 NumPy 배열 처리와 거의 비슷하다.
# - Pandas도 NumPy 배열을 기반으로 작성되었다.

# ### NumPy 배열 기본 조작

# - 배열 속성 지정
#     - 배열의 크기, 모양, 메모리 소비량, 데이터 타입을 결정한다.   
#    
# - 배열 인덱싱
#     - 개별 배열 요소값을 가져오고 설정한다.   
#    
# - 배열 슬라이싱
#     - 큰 배열 내에 있는 작은 하위 배열을 가져오고 설정한다.   
#        
# - 배열 재구조화
#     - 해당 배열의 형상을 변경한다.   
#       
# - 배열 결합 및 분활
#     - 여러 배얼을 하나로 결합하고 하나의 배열을 여러 개로 분할한다.

# #### 배열 속성 지정 : 배열의 크기, 모양, 메모리 소비량, 데이터 타입을 결정한다.

# In[22]:


np.random.seed( 0 ) # 재현 가능성을 위한 시드값 부여


# In[23]:


x1 = np.random.randint( 10, size = 6 ) # 1차원 배열
x2 = np.random.randint( 10, size = ( 3, 4 ) ) # 2차원 배열
x3 = np.random.randint( 10, size = ( 3, 4, 5 ) ) # 3차원 배열


# In[24]:


x1


# In[25]:


x2


# In[26]:


x3


# - 각 배열은 속성으로 ndim( 차원의 개수 ), shape( 각 차원의 크기 ), size( 전체 배열의 크기)를 가지고 있다.

# In[27]:


print( 'x1 ndim : ', x1.ndim ) # 차원의 개수
print( 'x1 shape : ', x1.shape ) # 차원의 크기
print( 'x1 size : ', x1.size ) # 전체 배열의 크기


# In[28]:


print( 'x2 ndim : ', x2.ndim ) # 차원의 개수
print( 'x2 shape : ', x2.shape ) # 차원의 크기
print( 'x2 size : ', x2.size ) # 전체 배열의 크기


# In[29]:


print( 'x3 ndim : ', x3.ndim ) # 차원의 개수
print( 'x3 shape : ', x3.shape ) # 차원의 크기
print( 'x3 size : ', x3.size ) # 전체 배열의 크기


# In[30]:


print( 'x1 dtype : ', x1.dtype ) # 배열의 type
print( 'x2 dtype : ', x2.dtype )
print( 'x3 dtype : ', x3.dtype )


# - itemsize : 각 배열 요소의 크기를 바이트 단위로 표시
# - nbytes : 배열 전체 크기를 바이트 단위로 표시. itemsize를 size로 곱한값과 동일

# In[31]:


print( 'x1 itemsize : ', x1.itemsize, 'bytes' )
print( 'x1 nbyte : ', x1.nbytes, 'bytes' )
print( 'x2 itemsize : ', x2.itemsize, 'bytes' )
print( 'x2 nbyte : ', x2.nbytes, 'bytes' )
print( 'x3 itemsize : ', x3.itemsize, 'bytes' )
print( 'x3 nbyte : ', x3.nbytes, 'bytes' )


# #### 배열 인덱싱 : 배열 요소에 접근하기

# ### https://numpy.org/doc/stable/user/basics.indexing.html

# In[32]:


x1


# In[33]:


x1[ 0 ]


# In[34]:


x1[ 4 ]


# In[35]:


x1[ -1 ] # 배열 끝에서부터 인덱싱하려면 음수 인덱스 사용


# In[36]:


x1[ -2 ]


# - 다차원 배열에서는 ,로 구분된 인덱스 튜플을 이용해 배열 항목에 접근할 수 있다.

# In[37]:


x2


# In[38]:


x2[ 0, 0 ]


# In[39]:


x2[ 2, 0 ]


# In[40]:


x2[ 2, -1 ] 


# - 인덱스 표기법을 사용하여 요소의 값을 수정할 수도 있다.

# In[41]:


x2[ 0, 0 ] = 12
x2


# - 파이썬 list와 달리 NumPy 배열은 고정 타입을 가진다는 점을 명심하자.
# - 예로 정수 배열에 부동 소수점 값을 기억시키면 그 값은 소수점 이하를 잘라버리고 저장한다.

# In[42]:


x1[ 0 ] = 3.141592
x1


# ### 배열 슬라이싱 : 하위 배열에 접근하기

# - []사용해 개별 배열 요소에 접근할 수 있는 것처럼 : 기호로 표시되는 슬라이스( slice ) 표기법으로 하위 배열에 접근할 수 있다.
# - NumPy 슬라이싱 구문은 표준 파이썬 리스트의 슬라이싱 구문을 따른다.
# - 배열 x 의 슬라이스에 접근하려면 다음 구문을 사용한다.   
# 
# x[ start : stop : step ]   
# 
# - 이 중 하나라도 지정되지 않으면 기본으로 start = 0, stop = 배열 차원의 크기, step = 1로 값이 설정된다.

# In[43]:


# 1차원 하위 배열
x = np.arange( 10 )
x


# In[44]:


x[ :5 ]


# In[45]:


x[ 5: ]


# In[46]:


x[ 4:7 ]


# In[47]:


x[ ::2 ]


# In[48]:


x[ 1::2 ]


# - step값을 음수로 부여했을 때 혼동이 올 수 있다. 이 경우에는 start와 stop의 기본값이 서로 바뀐다.
# - 이는 배열을 꺼꾸로 만드는 편리한 방법이 될 수 있다.

# In[49]:


x[ ::-1 ]


# In[50]:


x[ 5::-2 ]


# In[51]:


# 다차원 배열 슬라이싱
x2


# In[52]:


x2[ :2, :3 ]


# In[53]:


x2[ :3, ::2 ]


# In[54]:


x2[ ::-1, ::-1 ]


# ### 배열의 행과 열에 접근

# - 한 가지 공통으로 필요한 루틴은 배열의 단일 행이나 열에 접근하는 것이다.
# - 이것은 단일 콜론으로 표시된 빈 슬라이스를 사용핼 인덱싱과 슬라이싱을 결합함으로써 할 수 있다.

# In[55]:


print( x2[ :, 0 ] )


# In[56]:


print( x2[ 0, : ] )


# - 행에 접근하는 경우 더 간결한 구문을 위해 빈 슬라이스를 생략할 수 있다.

# In[57]:


print( x2[ 0 ] ) # x2[ 0, : ]와 동일


# ### 사본이 아닌 뷰로서의 하위 배열

# - 배열 슬라이스가 배열 데이터의 사본( copy )이 아니라 뷰( view )를 반환한다는 점
# - 이는 NumPy 배열 슬라이싱이 파이썬 리스트 슬라이싱과 다른 점으로 주의할 점
# - 파이썬 리스트에서 슬라이스는 사본이다.

# In[58]:


x2


# In[59]:


x2_sub = x2[ :2, :2 ] # 0~1행, 0~1열 2 x 2 크기의 하위 배열
x2_sub


# In[60]:


x2_sub[ 0, 0 ] = 99
x2_sub


# In[61]:


x2


# - 위와 같은 동작은 실제로 매우 유용하다.
# - 이것은 매우 큰 데이터세트를 다룰 때 기반 데이터 버퍼를 복사하지 않아도 이 데이터의 일부에 접근하고 처리할 수 있다는 뜻이다.

# ### 배열 사본 만들기

# - 배열 뷰의 기능의 유용해도 때로는 배열이나 하위 배열 내의 데이터를 명시적으로 복사하는 것이 더 유용할 때가 있다.
# - copy() 메서드를 이용하여 배열 명시적 복사를 수행할 수 있다.

# In[62]:


x2_sub_copy = x2[ :2, :2 ].copy()
x2_sub_copy


# In[63]:


x2_sub_copy[ 0, 0 ] = 42
x2_sub_copy


# In[64]:


x2


# ### 배열 재구조화

# - 배열의 형상을 변경하는 것이다.
# - reshape() 메서드를 사용한다.

# In[66]:


grid = np.arange( 1, 10 ).reshape( ( 3, 3 ) )
grid


# - 위 코드 동작시 초기 배열의 규모가 형상이 변경된 배열의 규모와 일치해야 한다.
# - reshape() 메서드가 초기 배열의 사본( copy )이 아닌 뷰( view )을 사용하겠지만, 연속되지 않은 메모리 버퍼일 경우에는 그렇지 않을 수도 있다.
# - 또 다른 일반적인 재구조화 패턴은 1차원 배열을 2차원 행이나 열 매트릭스로 전환하는 것이다.
# - 이 작업은 reshape() 메서드로 할 수 있으며, 그렇지 않으면 슬라이스 연산 내에 newaxis 키워드를 사용할 수도 있다.

# In[68]:


x = np.array( [ 1, 2, 3 ] )
x


# In[69]:


x.reshape( ( 1, 3 ) ) # reshape를 이용한 행 백터로 재구조화


# In[70]:


x[ np.newaxis, : ] # newaxis를 이용한 행 백터로 재구조화


# In[71]:


x.reshape( ( 3, 1 ) ) # reshape를 이용한 열 벡터로 재구조화


# In[72]:


x[ :, np.newaxis ] # newaxis를 이용한 열 벡터로 재구조화


# ## NumPy 배열 연산 : 유니버설 함수( universal function, ufuncs )

# - NumPy는 데이터 배열을 사용하여 최적화된 연산을 쉽고 유연한 인터페이스를 제공
# - NumPy 배열의 연산은 아주 빠르거나 아주 느릴 수 있다.
# - 이 연산을 빠르게 만드는 핵심은 벡터화( vectorized ) 연산을 사용하는 것이다.
# - 일반적으로 NumPy의 유니버설 함수( universal function, ufuncs )를 통해 구현
# - 배열 요소에 대한 반복적인 계산을 효율적으로 수행하게 해준다.   
# 
# - 벡터화 연산은 간단히 배열에 연산을 수행해 각 요소에 적용함으로써 수행할 수 있다
# - NumPy에서 벡터화 연산은 NumPy 배열의 값에 반복된 연산을 빠르게 수행하는 것을 주목적으로 하는 ufuncs를 통해 구현
# - ufuncs는 스칼라( 값 )와 배열 사이의 연산 및 두 배열 간의 연산도 가능하다.

# In[79]:


x = np.arange( 4 )
x


# In[80]:


print( 'x       = ', x )
print( 'x + 5   = ', x + 5 )
print( 'x - 5   = ', x - 5 )
print( 'x * 5   = ', x * 5 )
print( 'x / 5   = ', x / 5 )
print( 'x // 2  = ', x // 2 )
print( '-x      = ', -x )
print( 'x ** 2  = ', x ** 2 )
print( 'x %  2  = ', x % 2 )


# #### 집계 

# - 배열을 특정 연산으로 축소하고자 할 때 사용하는 메서드 : reduce()
# - reduce() 메서드는 결과가 하나만 남을 때까지 해당 연산을 배열 요소에 반복해서 적용한다.

# In[74]:


x = np.arange( 1, 6 )
x


# In[75]:


np.add.reduce( x )


# In[76]:


np.multiply.reduce( x )


# - 계산 중간 결과를 모두 저장하고 싶다면 accumulate() 메서드를 사용

# In[77]:


np.add.accumulate( x )


# In[78]:


np.multiply.accumulate( x )


# - 배열의 합 계산

# In[81]:


a = np.random.random( 100 )
a


# In[82]:


# 파이썬 내장 함수
sum( a )


# In[83]:


# NumPy 함수
np.sum( a )


# In[84]:


# 파이썬 내장 함수
min( a ), max( a )


# In[85]:


# NumPy 함수
np.min( a ), np.max( a )


# In[86]:


a.sum(), a.min(), a.max()


# - 다차원 집계

# In[87]:


M = np.random.random( ( 3, 4 ) )
M


# - 다차원 배열은 집계 연산 수행시 행이나 열을 기준으로 집계한다.

# In[88]:


M.sum()


# In[89]:


M.sum( axis = 0 )


# In[90]:


M.sum( axis = 1 )


# - 다차원 집계 합수는 어느 축( axis )을 지정하느냐에 따라 집계할 축을 결정할 수 있다. 
# - axis 키워드는 축소할 배열의 차원은 지정한다. 즉 축을 결정한다.
#     - axis = 0은 열을 지정
#     - axis = 1은 행을 지정 

# In[91]:


M.min( axis = 0 ) # 열에 대한 최소값


# In[92]:


M.min( axis = 1 ) # 행에 대한 최소값


# |함수명|NaN 안전 모드|설명|
#  |---|---|---|
#  |np.sum|np.nansum|요소의 합 계산|
#  |np.prod|np.nanprod|요소의 곱 계산|
#  |np.mean|np.nanmean|요소의 평균 계산|
#  |np.std|np.nanstd|표준 편차 계산|
#  |np.var|np.nanvar|분산 계산|
#  |np.min|np.nanmin|최소값 계산|
#  |np.max|np.nanmax|최대값 계산|
#  |np.argmin|np.nanargmin|최소값의 인덱스 찾기|
#  |np.argmax|np.nanargmax|최대값의 인덱스 찾기|
#  |np.median|np.nanmedian|요소의 중앙값 찾기|
#  |np.percentile|np.nanpercentile|요소의 순위 기반 백분위 수 계산|
#  |np.any|N/A|요소 중 참이 있는지 검사|
#  |np.all|N/A|모든 요소가 참인지 검사|

# In[ ]:




