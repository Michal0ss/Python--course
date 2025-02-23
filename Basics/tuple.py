# tuple = collection which is ordered and unchangeable used to group together related data

student = ("Bro", 21, "male")

print(student.count("Bro"))  # amount
print(student.index("male")) # place

for x in student: # display all
    print(x)
if"Bro" in student:
    print("Bro is here!")