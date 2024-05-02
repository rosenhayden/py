import math

def quadroots(a, b, c):
    d = discriminant(a, b, c)
    denom = 2 * a
    root1 = (-b + math.sqrt(d)) / denom
    root2 = (-b - math.sqrt(d)) / denom 
    return root1, root2



def discriminant(a, b, c):
    return (b ** 2) - (4*a*c)
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

r1, r2 = quadroots(a, b, c)
print(r1)
print(r2)
