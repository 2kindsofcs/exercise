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
#이름을 스트링으로 바로 넣어줄 수도 있겠지만, 다른 클래스의 인스턴스를 인수로 넣어줄 수 있다. 

myPerson2 = Person(Person_name("Sally", "Park"), "dark brown", 21)
#Person 클래스의 생성자로 Pereson_name의 인스턴스를 곧바로 넘겨버릴 수 있다. 
#이렇게 하면 코드를 줄일 수 있을 뿐더러 고작 1번 사용하고 다신 사용되지 않을 변수명을(이 경우 newname) 아낄 수 있다. 

print(myPerson1.name) # <__main__.Person_name object at 메모리주소>
print(myPerson1.name.firstname) # Jane
print(myPerson2.name.firstname) # Sally

def capitalizeName(name): #name을 인자로 받을 경우 name 하위에 있는 객체변수에 접근할 수 있으므로 예상하는 대로 upper 함수를 쓸 수 있다.
    name.firstname = name.firstname.upper()
    name.lastname = name.lastname.upper()

capitalizeName(myPerson1.name) 
print(myPerson1.name.firstname)
print(myPerson1.name.lastname)