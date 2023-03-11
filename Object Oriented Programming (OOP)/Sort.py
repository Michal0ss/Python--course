# sort() method = used with lists
# sort() function = used with iterables

students = ("Squidward", "Sandy", "Patrick", "Spongebob", "Mr.Krabs")

# students.sort(reverse = True) # works with lists []
sorted_students = sorted(students, reverse=True)  # sorted_students is a list but except iterable as an argument

# for i in sorted_students:
#    print(i)
# ---------------------------------------------------------------------
students1 = (
    ("Squidward", "F", 60),
    ("Sandy", "A", 33),
    ("Patrick", "D", 36),
    ("Spongebob", "B", 20),
    ("Mr.Krabs", "C", 78)
)

# grade = lambda grades: grades[1]  # that variable helps with sorting our iterables by the second column
age = lambda ages: ages[2]
#students1.sort(key=age, reverse=True)  # sort method only belongs to lists
sorted_students1 = sorted (students1, key =age, reverse=True) # for tuple

for i in sorted_students1:
    print(i)
