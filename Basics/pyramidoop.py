def play_again():
    response = input("Do you want to play again? (yer or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False


class Pyramid:
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
#.............................