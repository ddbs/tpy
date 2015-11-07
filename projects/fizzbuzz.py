#!/usr/bin/env python3

import sys

print("The name of this script is {}".format(sys.argv[0]))
print("User supplied {} arguments at run time".format(len(sys.argv)))
for arg in sys.argv[1:]:
    print(arg)

try:
    n = int(sys.argv[1])
except:
    while True:
        try:
            n = input("Please provide a valid number: ")
            n = int(n)
        except ValueError:
            print("Invalid number!")
        else:
            break

print("Fizz buzz counting up to", n)
for n in range(1, n+1):
    if n%3 == 0 and n%5 == 0:
        print("Fizz Buzz")
    elif n%5 == 0:
        print("Buzz")
    elif n%3 == 0:
        print("Fizz")
    else:
        print(n)
