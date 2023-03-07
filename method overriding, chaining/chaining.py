# method chaining = calling multiple methods sequentially each call performs
#                   an action on the same object and returns self

class Car:
    def turn_on(self):
        print("You start the engine")
    def drive(self):
        print("You drive the car")
    def brake(self):
        print("You step on the brakes")
    def turn_off(self):
        print("You turn off the engine")
