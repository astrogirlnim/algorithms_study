#15
import math


def routes(n):
    """
    Calculates the number of routes, only being able to move right and down,
    from the top left to bottom right corners of an nxn grid.
    Assuming n >= 2.
    """
    return (math.factorial(n*2)/math.factorial(n)**2)

n = int(input())
print(routes(n))

