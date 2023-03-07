# str.format()= optional method that gives users more control when displaying output


animal = "cow"
item = "moon"

# print("The {} jumped over the {}".format(animal, item))
# print("The {1} jumped over the {0}".format(animal, item)) #opositional argument
# print("The {animal} jumped over the {item}".format(animal ="cow", item = "moon")) #keyword argument

# text = "The {} jumped over the {:10}. And fell over"
# text1 = "The {} jumped over the {:>10}. And fell over"
# text2 = "The {} jumped over the {:<10}. And fell over"
# text3 = "The {} jumped over the {:^10}. And fell over"
# print(text.format (animal, item))
# print(text1.format (animal, item))
# print(text2.format (animal, item))
# print(text3.format (animal, item))

number = 1000
print("The number pi is {:.2f}".format(number))
print("The number pi is {:,}".format(number))
print("The number pi is {:b}".format(number))
print("The number pi is {:o}".format(number))
print("The number pi is {:x}".format(number))
print("The number pi is {:e}".format(number))