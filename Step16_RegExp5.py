# Step16_RegExp5.py

import re


if __name__ == "__main__":
    input_id = input("아이디 입력(영문자로 시작하고, 5-10 글자 이내, 특수문자 허용안함):")
    
    # 위에 조건 맞을시 "가입되었습니다" 아니면 "사용할수 없는 아이디 입니다"
    pattern = r"^[a-zA-Z][a-zA-Z0-9]{4,9}$"
    

if re.search(pattern, input_id):
   print("가입되었습니다")
else:
    print("사용할수 없는 아이디 입니다")