# zip(*iterables) = aggregate elements from two or more iterables
# creates a zip object with paired elements stored in tuples for each element within zip object

usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abc123", "guest")

users = dict(zip(usernames, passwords))  # sign as a dictionary

print(type(users))

for key, value in users.items():
    print(key + " " + value)

# --------------------------------------------------------------

usernames1 = ["Dude", "Bro","Mister"]
passwords1 = ("p@ssword", "abc123", "guest")
login_date = ["1/1/2023","1/2/2023","1/3/2023" ]

users1 = zip(usernames1,passwords1,login_date)

for i in users1:
    print(i)