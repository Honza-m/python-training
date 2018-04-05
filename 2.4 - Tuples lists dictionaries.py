# standard variables
x = 1
y = 2

# tuples
# Allow for more variables to be stored under one label
# Once defined can't be changed (immutable)

def tuples_test():
    x = ('a', 'b', 'c')
    x = ('a', 2, 2)
    print(x)

    y = ('a', x)
    print(y)

def access_tuple():
    x = ('a', 'b', 'c')
    print(x[0]) # zero-indexed!
    print(x[-1]) # reversed is one-indexed

def access_more():
    x = ('a', 'b', 'c')
    print(x[0:2])
    print(x[:2])
    print(x[1:])
    print(x[:-1])

def access_error():
    x = ('a', 'b', 'c')
    print(x[5]) # will raise IndexError

# lists
# Same as tupples but can be changed once defined
def define_list():
    x = ['a', 'b', 'c']
    print(x)

def mutate_list():
    x = ['a', 'b', 'c']
    x[0] = ['OMG']
    print(x)

def append_list():
    x = ['a', 'b', 'c']
    x.append('d')
    print(x)

def extend_list():
    list_a = ['a', 'b', 'c']
    list_b = ['d', 'e', 'f']

    list_a.extend(list_b)
    print(list_a)

def delete_from_list():
    #del
    x = ['a', 'b', 'c']
    del x[0:2]
    print("del:", x)

    #remove
    x = ['a','b','c']
    x.remove('c')
    print("remove: ", x)

    #pop - deletes and returns last element
    x = ['a','b','c']
    last = x.pop()
    print("pop: ", last)

    #clear - removes everything from the list
    x = ['a','b','c']
    x.clear()
    print("clear: ", x)


# Changing tuples to lists and vice versa
# If you need to make immutable mutable
def change_test():
    x = (1, 2, 3)
    y = list(x)
    print(x)
    z = tuple(y)
    print(z)

delete_from_list()
