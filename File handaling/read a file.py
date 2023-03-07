
x= input("Write your file: ")
try:
    with open(x) as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found")