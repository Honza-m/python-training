#definitions
def string_def():
    x = 'This is a string'
    print(x)
    x = "This is also a string"
    print(x)
    z = """ This
    is
    a multiline
    string - good for documentation!"""
    print(z)

def special_chars():
    x = "What is I want \"quotes\"?"
    print(x)
    x = "C:\\Users\\Jan"
    print(x)

def string_methods():
    """ https://docs.python.org/3.6/library/string.html """
    x = "   this IS a long sentence    "

    print(x.upper())
    print(x.lower())
    print(x.lstrip())
    print(x.rstrip())
    print(x.strip())
    print(x.replace('IS','IS NOT'))
    print()


    x = "test"
    print(x.capitalize())

def format_string(x, y):
    result1 = "This is the first arguement: {}".format(x)
    print(result1)
    result2 = "These are your arguments: {}, {}".format(x, y)
    print(result2)

string_methods()
