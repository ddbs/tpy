#!/usr/bin/env python3

def subtractor(a, b):
    """subtract a from b and return the result"""
    print("I'm a function. My name is {}".format(subtractor.__name__))
    print("I'm about to subtract {} and {}\n\n".format(a, b))
    return a - b


# from other file, import function from this_file.py:
# from this_file import subtractor
# my_function = subtractor  ## without the parenthesis!
# my_function(3,2)


def print_function():
   """I'm also a function, but I don't take any parameters"""
   print("I'm {}, and I'm printing now!".format(print_function.__name__))


def function3(a=1, b=1):
    """I'm a function that calls other functions"""
    print("I'm {} and I'm about to call other function".format(function3.__name__))
    total = subtractor(a, b)
    print("I'm {} and I'm about to call print_function".format(function3.__name__))
    print_function()
    print("I'm {} and I'm about to return total".format(function3.__name__))
    return total

#total = function3()
#print("Total is {}".format(total))


def side_effect_test(value):
    """Test how changes to value inside the function affects its value outside of
    the function"""
    value[1] = "orange"
    print("Inside the function, the value becomes {}".format(value))


# run this file from command line
if __name__ == '__main__':
    value = ["red", "green", "blue"] # create the value
    print("Outside the function, the value starts as {}".format(value))
    side_effect_test(value)
    print("Outside the function the value is now {}".format(value))
