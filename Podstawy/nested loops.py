# nested loops = the inner loop will finish all of its iterations before finishing one iteration of the outer loop
#1:17:32
#rows = int(input("how many rows?: "))
#columns = int(input("how many columns?: "))
#symbol = input("enter a symbol to use: ")

#for i in range (rows):
#    for j in range(columns):
#        print(symbol, end="")
#    print()

#rows = int(input("how many rows?: "))
#columns = int(input("how many columns?: "))
numbers = int(input("enter how many letters: "))

for i in range(numbers):
    for j in range(i+1):
        print(i+1, end="")
    print()
