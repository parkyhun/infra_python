# Step04_Str02.py

"""

"""

#json 형식 javascript 객체 표기법을 따르는 문서 형식이다 (비우고 싶다면 null)
# json 모듈  import 하기
import json
from operator import rshift

# info 는 str type 이긴 한데 문자열이 특별한 형식(json)을 띄고 있다
info = '''{
    "name":"이정호",
    "addr":"노량진",
    "foods":["맥주","베이컨"]   
}'''

# resilt 는 str(json형식) 의 문자열이 python 의 dict 로 변경된 값을 가지고 있다
# json에서 python dict로 변환시 사용 
result = json.loads(info) 

print(result["name"])
print(result["addr"])
print(result["foods"])
print(result["foods"][0])
print(result["foods"][1])

# dict 에 저장된 데이터를 json 문자열로 변환 
result2 = json.dumps(result)



print("종료됨")
