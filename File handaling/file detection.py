import os
path = "C:\\Users\\smiec\\Desktop\\folder"
if os.path.exists(path):
    print("that location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("that is a directory")
else:
    print("that locations doesnt exist")