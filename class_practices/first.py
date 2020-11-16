"""
08/18class 추가수업
===============
Created 화요일 18 8월 2020

파이썬에서는 모든것이 객체이다.

type 으로 확인을 해보면 모든것은 클래스의 인스턴스라는것을 확인 할 수 있다.


캡슐화: 데이터와 알고리즘을 하나로 묶어 공용 인터페이스만 제공하고 세부 사항을 감추는 것.
			 (java 에서는 이를 private 라는 속성값으로 사용)


"""
# 켑슐화에 대한 설명

class People:
    def __init__(self, age=0, name=None):
        self.__age = age
        self.__name = name
    
    def getAge(self):
        return self.__age
    def getName(self):
        return self.__name
    def setAge(self, age):
        self.__age = age
    def setName(self, name):
        self.__name = name
        
        
p1 = People(20, "KIM")
print(p1.getAge())

