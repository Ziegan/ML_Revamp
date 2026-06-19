from os import name

##BASIC CLASS
class Test:
    a = 1

a1 = Test()
print(a1.a)
del a1

##CLASS WITH ARGS
class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

p1 = Person("Ziegan", 29)
p2 = Person("Wesley")

print(p1.name, p1.age)
print(p2.name, p2.age)

##CLASS WITH FUNCTION
class person:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age
        self.works = ""
        print("Class Initialization Success")
    
    def __str__(self):
        return f"Object values {self.name, self.age}"
    
    def greeting(self):
        print(f"Welcome {self.name}")

    def character(self):
        self.greeting()
        print(f"{self.name} Loves Dressings, Travelling and Coding and is in his {self.age}")
    
    def future(self, future):
        print(f"{self.name} will be {self.age + future} in {future} years")

objects = person("Wesley")
print(objects)

objects.character()

objects.age = 29
objects.character()

objects.future(1)