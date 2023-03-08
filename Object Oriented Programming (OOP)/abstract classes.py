# Prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class

# abstract class = a class which contains one or more abstract methods
# abstract method = a method that has a declaration but does not have an implementation

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        print("You drive the car")
    @abstractmethod
    def stop(self):
        print(2+2)
class Car(Vehicle): #overreading
    def go(self):
        print("You drive the car")
    def stop(self):
        print("This car is stopped")
class Motorcycle(Vehicle):#overreading
    def go(self):
        print("You ride the motorcycle")
    def stop(self):
        print("This motorcycle is stopped")
#vehicle = Vehicle()
car=Car()
motorcycle=Motorcycle()

#vehicle.go()
car.go()
motorcycle.go()
car.stop()
motorcycle.stop()