

##############################################################################
# STRINGS
##############################################################################


print("{0} don't think it {1} like it is, but it {2}".format("They", "be", "do"))

print("Yar matey!"[0])


##############################################################################
# LISTS
##############################################################################

# lists retain the order

#empty list
li = []

#pre-filed list
li = [1, 2, 5, 4]

# add element to list\
li.append(9)

# remove end element from list
li.pop()

# Select a range between index 1 and 3 (closed/open range, in math terms)
li[1:3]

# Omit the beginning or end
li[2:]
li[:3]

# Select every second entry (i.e. step by 2)
li[::2]

# Reverse the list
li[::-1]

# Delete the 3rd item
del li[2]

# Search the list li to see if 1 is in it
1 in li
True

# What's the length of the list li?
len(li)

##############################################################################
# TUPLES
##############################################################################
# tuples are immutable lists

tup = (1, 2, 3)

new_tup = tup + (4,5,6)

# a list with tuples
bookmark1 = (35, 5)
bookmark2 = (86, 15)
bookmark3 = (106, 11)
notes = [bookmark1, bookmark2, bookmark3]

##############################################################################
# SETS
##############################################################################
# sets contain unique values, ordered

my_set = {1, 2, 2, 3, 4, 5, 6, 7}


##############################################################################
# DICTIONARIES
##############################################################################
# sets contain unique values, ordered

stooges = {"Larry": "balding, with frazzled hair",
    "Curly": "short buzz-cut",
    "Moe"  : "bowl cut"}

# access an element in the dictionary
stooges['Larry']

# get all the keys
stooges.keys()

# get all the values
stooges.values()

# check if an element is in the dict
"Larry" in stooges

# get an element; DO NOT RETURN ERROR if not found
stooges.get("Shemp")
