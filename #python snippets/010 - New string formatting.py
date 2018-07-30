""" There are many different ways of getting variables into your strings.
    But the new f"" string beats them all (most of the time anyway).
"""

# Variables
age = 7
name = "Dean"

# All of the following strings will yield the same text - 'My name is Dean and I'm 7 years old.'
# They're just different ways of getting vatiables into the stings.

# BEFORE
text = "My name is " + name + " and I'm " + str(age) + " years old."

# OR MAYBE
text = "My name is {} and I'm {} years old.".format(name, age) # Notice no str() needed for age .format handles this.

# BUT NOW! (notice the 'f' before the start of the string - signifies this is a formatted string)
text = f"My name is {name} and I'm {age} years old." # So short, much wow.
