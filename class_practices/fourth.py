"""
다형성(polymorphism)
"""

class Korean():
    def greeting(self):
        print("HHEELLOOOOO")


class American():
    def greeting(self):
        print("hello")
        
def sayhello(people):
    people.greeting()
    
kim = Korean()
john = American()
sayhello(kim)
sayhello(john)
print(kim.__str__())