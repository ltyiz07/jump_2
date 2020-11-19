"""
클래스를 정의할 때 class ClassName: 과 class ClassName(object): 는 동일하다.

__new__() 메소드는 객체가 생성될 때 자동으로 호출된다.
__init__() 는 그다음^^

__str__() 메소드는 객체의 클래스 이름과 객체의 메모리 
주소로 구성된 객체에 대한 설명을 문자열로 반환한다
"""

class People():
    def __init__(self, age=0, name=None):
        self.__age = age
        self.__name = name
        
    # def __str__(self):
    #     return super().__str__()
        
    def __str__(self):
        return "info -- name : " + self.__name + " age : " + str(self.__age)
        
        
p1 = People(20, "Lee")
print(p1)
