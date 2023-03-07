# exception = events detected execution that interrupt the flow of a program

try:
    numerator = int(input("Enter a nr to divide: "))
    denominator = int(input("Enter a number to divide by"))
    result = numerator / denominator
except ZeroDivisionError as e:
    print("U cant divide by zero idiot")
except  ValueError as e:
    print("Enter only numbers pls")
except Exception as e:
    print(e)
    print("Sth went wrong")
else:
    print(result)
finally:
    print("this will always execute")