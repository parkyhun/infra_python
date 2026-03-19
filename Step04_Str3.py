# yaml 형석의 문자열 다루기

# yaml 문자열을 다룰때는 외부 모듈을 pip 로 설치를 해서 import 를 해야 한다.
# python 가상환경을 구성하고 pip install pyyaml 설치후


import yaml

info = '''
name: 박영헌
addr: 안산
foods:
  - 맥주  
  - 베이컨
isMan: true
body: 
  weight: 75 
  height: 174  
'''



# info 에 들어 있는 문자열을 dict type 으로 바꾸세요
# 다음 dict 에 들어 있는 내용을 확인 후 다시 dict 에 있는 내용을 이용해서 yaml 문자열 형식으로 변환하시오

result = yaml.safe_load(info) # 문자열에서 dict 변환하는 방법
print(result)



result2 = yaml.dump(result,allow_unicode=True,sort_keys=False)
print(result2)

print("종료합니다")


#yaml_str = yaml.dump(data, allow_unicode=True, sort_keys=False) #dict에서 yaml 문자열로 변환 방법 

#print(yaml_str)
#print(type(result))