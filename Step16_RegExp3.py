# Step16_RegExp3.py

import re


logs = [
    "[INFO] Server started successfully.",
    "[WARN] Memory usage is high.",
    "[ERROR] Database connection failed.",
    "[DEBUG] x = 10"
]

# logs 에서 ERROR or WARN 로그만 찾아서 콘솔창에 출력해 보세요


for log in logs:
    if re.search(r"ERROR|WARN", log):
        print(log)



