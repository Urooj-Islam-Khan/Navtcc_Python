import math

def quadraticFormula(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real roots"  
    root = math.sqrt(discriminant)
    eq1 = (-b - root) / (2 * a)  
    eq2 = (-b + root) / (2 * a)  
    return eq1, eq2

print(quadraticFormula(1, 2, 3))  
print(quadraticFormula(1, -3, 2))  