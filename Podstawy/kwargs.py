# **kwargs = parameter that will pack all arguments into a dictionary useful so that a function can accept a varying
# amount of keyword arguments

def hello(**kwargs):
    # print("Hello "+kwargs['first']+" "+kwargs['last'])
    print("Hello", end=" ")
    for key, value in kwargs.items(): # key,value - needed
        print(value, end=" ")


hello(title = "3", last=5, middle=2*3, first="Code") #keyword arguments
