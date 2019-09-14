'''class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, i am {self.name}")


John = Person("John Smith")
John.talk()

Wolf = Person("Wolf")
Wolf.talk()'''

#HERANÇA
class Mammal:
    def walk(self):
        print("Walk")


class Dog(Mammal):
    def bark(self):
        print("Woof, woof")


class Cat(Mammal):
    pass


dog1 = Dog()
dog1.bark()
