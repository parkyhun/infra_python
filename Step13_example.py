# Step13_example.py

from jinja2 import Template


info:dict = {
    "num":1,
    "name":"김구라",
    "body":{
        "height": 180,
        "weight": 80
    },   
    "hobby":["피아노","당구","프로그래밍"]
}

'''
번호: 1
이름: 김구라
키: 180 cm
몸무게: 80 KG
취미: 
-피아노 
-당구
-프로그래밍
'''

info_template = '''
    번호: {{ num }}
    이름: {{ name }}
    키: {{ body.height }} cm
    몸무게: {{ body.weight }} KG
    취미:
    {% for hobb in hobby %}
    - {{ hobb }}
    {% endfor %}
'''
temp: Template = Template(info_template)
result: str = temp.render(info)

print(result)