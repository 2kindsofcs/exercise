class Person:
    def __init__(self, name, eyecolor, age):
        self.name = name
        self.eyecolor = eyecolor 
        self.age = age 

class Person_name:                                 
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

newname = Person_name("Jane","Kim")
myPerson1 = Person(newname, "dark brown", 21)

myPerson2 = Person(Person_name("Sally", "Park"), "dark brown", 21)
#Person 클래스의 생성자로 Pereson_name의 인스턴스를 곧바로 넘겨버릴 수 있다. 
#이렇게 하면 코드를 줄일 수 있을 뿐더러 고작 1번 사용하고 다신 사용되지 않을 변수명을(이 경우 newname) 아낄 수 있다. 

print(myPerson1.name) # <__main__.Person_name object at 메모리주소>
print(myPerson1.name.firstname) # Jane
print(myPerson2.name.firstname) # Sally
