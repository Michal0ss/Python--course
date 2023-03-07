def pyramid1(n):
    for i in range(0, 9):
        for j in range(0, n - i - 1):
            print(end=" ")
        for k in range(0, 2 * i + 1):
            print(i + 1, end="")
        print()

def pyramid2(n):
    for i in range(10, n + 1):
        for j in range(0, n - i):
            print(end=" ")
        for k in range(0, i - 1):
            print(i, end="")
        print(int(i / 10))

while True:
    n = int(input("enter how many numbers: "))
    if n != 0 and n != 1:
        break

pyramid1(n)
pyramid2(n)
#sprobowac uzyc random do utworzenia piramidy z randomowych lub pomieszanych z tablicy znakow liczb
#uzyc exceptions