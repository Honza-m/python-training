### TRY AND EXCEPT ###

def test1():
    while True:
        x = input("Please insert an integer > ")
        try:
            x = int(x)
            print("Thanks")
            break
        except ValueError:
            print('This is not an integer!')

def test2():
    x = 2 / 0
    print(x)

def test3():
    try:
        x = 2 / 0
        print(x)
    except:
        print("Error, please contact the IT.")
