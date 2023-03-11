# Higher Order Function = a function that either:
# 1. accepts a function as an argument
# 2. returns a function (in python, functions are also treated as objects)

def loud(text):
    return text.upper()


def quiet(text):
    return text.lower()


def hello(func):
    textx = func("Hello")
    print(textx)


hello(loud)  # function as an argument
hello(quiet)

# -------------------------------------------------
# returns function

def divisor(x):
    def dividend(y):
        return y/x
    return dividend

divide = divisor(2)
print(divide(10))