# multi-level inheritance = when a derived (child) class inhertits another derived (child) class

class Organism: #1
    alive = True


class Animal(Organism):#2
    def eat(self):
        print("This animal is eating")

class Dog(Animal):#3
    def bark(self):
        print("This dog is barking")





dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()
