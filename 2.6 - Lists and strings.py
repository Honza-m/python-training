SENTENCE = "Blue elephant on Rhode Island"

def string_to_list_tuple():
    print(list(SENTENCE))
    print(tuple(SENTENCE))

def split_string():
    r = SENTENCE.split(" ")
    print(r)

def join_to_string():
    x = ['h','e','l','l','o']
    r = "".join(x)
    print(r)
