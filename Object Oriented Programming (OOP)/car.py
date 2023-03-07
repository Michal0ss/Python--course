# Object = instance of a class
# attributes = what an object is/has name, age, height
# methods = what an object can do
# ----------------------------------------------------
class Car:
    wheels = 4  # class variable, default value for all instance of this class

    def __init__(self, make, model, year, color):  # this method construct object for us (constractor)
        self.make = make  # assign these object to an attributes
        self.model = model  # instance variable
        self.year = year  # instance variable
        self.color = color  # instance variable

    def drive(self):  # methodes #self is an argument
        print("This " + self.model + " is driving")

    def stop(self):
        print("This " + self.model + " has stopped")
