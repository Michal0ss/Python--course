class Animal:
    alive = True

    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eating a carrot")

rabbit = Rabbit()
rabbit.eat()     #an object will use a method that is more closely assiosiated with itself before relying on parent class