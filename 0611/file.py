#
# file 처리
#   : 메모리 내용을 보조 기억 장치의 파일에 보관하거나
#     보조 기억 장치에 저장된 파일 내용을 메모리에 저장 하는 모든 처리
#
# file 처리 절차
#   1. 파일 open
#   2. 파일 처리( 파일에서 읽기 / 파일에 쓰기 )
#   3. 파일 close
#
# 파일 종류( 저장되는 값의 형태에 따른 구분 )
#   1. Text file : ASCII 형태로 저장, 파일 끝을 의미하는 EOF가 저장됨
#                  데이터 양이 적고, 보안이 중요하지 않은 경우
#   2. Binary file : 메모리 내용( 2진수 형태 ) 그대로 저장
#                    파일의 끝을 의미하는 값이 저장되는 않음
#                    데이터 양이 많고, 보안이 중요한 경우
#
# 파일 종류( 한번에 저장되는 data 형식에 따른 구분 )
#   * record : 파일에 대해 한번에 읽기/쓰기 하는 단위
#   1. 고정 길이 레코드 : 레코드 길이가 일정하다. 검색이 쉬움
#   2. 가변 길이 레코드 : 레코드 길이가 일정하지 않다.
#                         저장 공간을 적게 차지한다.
#
# 파일 종류( 검색 방식에 따른 분류 )
#   1. 순차 파일 : record를 순차적으로 저장, 검색시 오래 걸림
#                  구현하기 쉬움
#   2. 색인 순차 파일 : record 저장 파일과 index(색인) 저장 파일로 저장
#                       검색이 빠름
#   3. 직접 파일 : record를 임의 위치에 저장, 검색 빠름, 구현 어려움
#
# 파일 쓰기
print( '파일 쓰기' )
#f = open( 'filetest.txt', 'a' )
with open( 'filetest.txt', 'a' ) as f:
    f.write( 'Python is great!!!' )
    f.write( '\n' )
#f.close()

# 파일 읽기
print( '파일 읽기' )
#f = open( 'filetest.txt', 'r' )
with open( 'filetest.txt', 'r' ) as f:
    text = f.read()
    print( 'filetest.txt로 부터 읽은 내용 : {}'.format( text ) )
#f.close()













