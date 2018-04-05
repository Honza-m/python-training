### COMMON ERRORS ###

# def invalid_syntax:
#     return "test"

def type_error_test(x):
    """ Only certain types can be combined together """
    return x + 3

def name_error_test(x):
    """ All variables need to be defined """
    return y

def zero_division_error(x):
    """ Can't divide by zero """
    return x / 0

def value_error_test(x):
    """ Accepts type string but needs to be a number """
    return int(x)

value_error_test("asd")
