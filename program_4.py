#write a program to find roots of a quadratic equation
import math
def find_roots(a,b,c):
    d = b**2 - 4*a*c
    if d > 0:
        root1 = (-b + math.sqrt(d)) / (2*a)
        root2 = (-b - math.sqrt(d)) / (2*a)
        return (root1, root2)
    elif d == 0:
        root = -b / (2*a)
        return (root,)
    else:
        return None
