#Step06_Tuple.py

'''
1. list type 과 유사
2. 읽기 전용 (수정, 삭제 불가)
3. 기능이 적기 때문에 처리 속도가 빠르다

방법 
(value1, value2, value3,....)
'''

# 3개의 str type 데이터를 tuple에 순서대로 담고
# 그 객체의 참조값을 tuple type tuple1 이라는 변수에 담기
tuple1: tuple = ("one", "two", "three")

result1 = tuple1[0]
result2 = tuple1[1]
result3 = tuple1[2]

# 방 1개짜리 tuple type 을 만들때는 주의
tuple2 = ("김구라",) # 하나짜리 만들시 뒤에 , 추가 

# 괄호 없는 튜플 생성
tuple3 = 10, 20, 30

# yuple 에 저장된 값을 여러 변수에 나누어 담기
a, b, b = tuple3

# 두 변수에 있는 값을 서로 바꾸려면?
first = "girl"
second = "boy"

tmp=first
first=second
second=tmp

# 위 3줄을 아래와 같이 가능
first, second = second, first


print("종료")

