#dict type 

"""
- dict type
1. key:value 형태로 데이터를 저장한다
2. 순서가 없는 데이터 이다.
3. key 

"""
# 회원 1명의 데이터 (list type)
mem1 = {"num":1, "name":"kimgura", "isMan":True}
# 회원 1명의 데이터(쓰기 어렵다)

#info1 = [1, "kimgura", True]
print(mem1["num"])
print(mem1["name"])
print(mem1["isMan"])

# dict 안에 내용을 참조해서 변수에 담기
a = mem1["num"]
b = mem1["name"]
c = mem1["isMan"]

# dict 안에 내용을 수정하기
mem1["num"] = 2
mem1["name"] = "park"
mem1["isMan"] = False

# 특정 key 값으로 저장된 내용 삭제
del mem1["isMan"]

# 모든 값 삭제
mem1.clear()

print("종료합니다")
