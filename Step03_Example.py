# Step03_Example.py

"""
   회원 한명의 정보는 번호, 이름, 주소 로 이루어 있다. - dict
   그리고 그러한 회원이 여러명이다.
   여러명의 회원 목록을 하나의 묶음으로(하나의 data) 로 관리하고 싶다면... -list
"""

# 3명의 회원정보를 각각 dict 에 담은 다음 그 dict 를 list 에 담는 코드를 작성해서 쳇팅창에 보내세요.
mem1 = {"num":1, "name":"kim", "add":"서울"}
mem2 = {"num":2, "name":"park", "add":"부산"}
mem3 = {"num":3, "name":"go"," add":"안산"}
# dict 3개를 list 에 담기
members = [mem1, mem2, mem3]

a = members
b = members[0]
c = members[0]["num"]
d = members[0]["name"]


print("종료됩니다.")
