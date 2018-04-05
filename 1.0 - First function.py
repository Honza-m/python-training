def area_comparer(x:float, y:float) -> str:
    """ Calculates area of a square from x & y coordinates and returns an info
        message
        Args: x - length of the square (metres)
              y - height of the square (metres)
    """

    result = x * y
    if result > 50:
        return "Square is bigger than 50m²"
    elif result == 50:
        return "Square is equal to 50 m²"
    else:
        return "Square is smaller than 50 m²"

print("### AREA COMPARER ###")
x = input("Please insert the length of the square in metres > ")
y = input("Please insert the height of the square in metres > ")

answer = area_comparer(float(x), float(y))
print(answer)
