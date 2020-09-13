"""
부모 클래스의 메소드를 그대로 이어 받아 사용하려면 자신의 메소드 이름
앞부분에 super(). 을 붙이고 매개변수에서는 self를 빼고 사용한다.
"""

class People:
    def __init__(self, age=0, name=None):
        self.__age = age
        self.__name = name
    
    def introMe(self):
        print("Name:", self.__name, "age:  ", str(self.__age))
        
        
class Teacher(People):
    def __init__(self, age=0, name=None, school=None):
        super().__init__(age, name)
        self.__school = school
        
    def showSchool(self):
        print("My school: ", self.__school)
        
p1 = People(20, "KIM")
print(p1.introMe())

t1 = Teacher(45, "Lee", "Highschool")
t1.introMe()
t1.showSchool()
