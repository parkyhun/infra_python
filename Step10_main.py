# Step10_main.py

'''
현재 파일 즉 Step10에서 run 실행시
__name__은 "__main__" 이라는 문자열이 들어있다
따라서 ___name__ 을 확인해 보면 해당 파일이  main 으로 실행되었는지 여부를 알수 있다
다른 곳에서 import 했을때 실행되지 않는 코드 블럭을 만들때 사용한다.
'''
print("Step10_main.py 가 실행됩니다")
print(__name__)

# 테스트 용도의 클래스 작성하기
class TestClass:
    pass

# 아래의 if 문 블럭은 main으로 실행되었을때만 실행된다(다른 곳에서 import 했을때는 실행되지 않는다)
if __name__ == "__main__":
    print("시작합니다")
    print("어떤 작업을 하고")
    print("종료 합니다")
    