text = "\nHave a nice day\n"
with open('test.txt', 'a') as file: #'w' - overwritten, 'a' - append
    file.write(text)