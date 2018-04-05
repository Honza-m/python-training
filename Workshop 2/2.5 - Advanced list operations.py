x = ['a', 'a', 'b', 'c']

def count_test():
    #count - counts the appearance of an element in the list
    r = x.count('a')
    print("count: ", r)

def len_test():
    #len - returns length of list
    l = len(x)
    print("Len: ",l)

def index_test():
    #index - returns position of first found element
    print("index: ", x.index('a'))

def in_test():
    #in - is the element in the list?
    if 'a' in x:
        print("Element is in the list")
    else:
        print("Element not in the list")

    print('a' in x)

def all_of_this_works_for_strings_as_well():
    x = 'Very long and complicated string'
    print(x[:5])
    print('Very' in x)
    print(len(x))
    print(x.count('o'))
    print(x.index('l'))
