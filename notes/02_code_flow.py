#!/usr/bin/env python3

# if
if 5 < 3:
    print("Things might be a little off...")
else:
    print("Yep, math works today.")


# if/elif
if 5 < 3:
    print("Things might be a little off...")
elif 5 == 3:
    print("Maybe we should stay inside.")
else:
    print("Yep, math works today.")


# Write if statements which tell you which record label the popular beat combo
# Ted Leo and the Pharmacists were signed to at a certain year. Note: 2001-2006
# was Lookout Records, 2007-2009 was Touch and Go Records,
# and 2010- is Matador Records

year = 2005
if year >= 2001 or year <= 2006:
    print("Lookout records")
elif year >= 2007 or year <= 2009:
    print("Touch and Go records")
elif year >= 2010:
    print("Matador Records")
else:
    print("No year with records")

# for with a tuple
beatles = ("John", "Paul", "George", "Ringo")
for beatle in beatles:
    print(beatle)


# for with a dictionary, print values and keys
actors = {
    "Kyle MacLachlan": "Dale Cooper",
    "Sheryl Lee": "Laura Palmer",
    "Lara Flynn Boyle": "Donna Hayward",
    "Sherilyn Fenn" : "Audrey Horne"}
for key, value in actors.items():
    print(key, value)


# while
miles_run = 0
running = True

while running:
    if miles_run <= 10:
        print("still running on mile {}".format(miles_run))
        miles_run += 1
    else:
        running = False

print("Finally!")


# Use a while loop to solve the following problem: A slow, but determined,
# walker sets off from Leicester to cover the 102 miles to London at 2 miles
# per hour. Another walker sets off from London heading to Leicester going at
# 1 mile per hour. Where do they meet?

miles_walked = 0
walker1 = 0
walker2 = 102
meeting = False

while miles_walked <= 102 and meeting == False:
    walker1 += 2
    walker2 -= 1
    print("walker1 {}, walker2 {}".format(walker1, walker2))
    if walker1 == walker2:
        meeting = True
    miles_walked += 1


# try
a = 1
b = 0
try:
    a / b
except ZeroDivisionError:
    print("Cannot divide by zero.")


# Try looking up Jamie Theakston in the following phone book. When it fails,
# catch the exception and print an appropriate error message.

phone_book = {
    "Sarah Hughes": "01234 567890",
    "Tim Taylor": "02345 678901",
    "Sam Smith":  "03456 789012"
}

try:
    phone_number = phone_book["Jamie Theakston"]
    print(phone_number)
except:
    print("No such name!")
