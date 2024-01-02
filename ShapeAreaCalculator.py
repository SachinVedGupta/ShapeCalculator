
#Calculate the area of any shape!

print(" ")
print(" ")
print(" ")

UserShape = input("Choose A Shape To Be Measured (Find The Area): Square, Cube, Rectangle, Rectangular Prism, Triangle, Triangular Prism, Pythagorean Theorem, Circle, Sphere:     ")

print(" ")
print(" ")


if UserShape == "Square":
    squaresidelength = float(input("Type Side Length of Square: "))
    print(" ")
    print("Area of Square = ")
    print(squaresidelength*squaresidelength)


if UserShape == "Cube":
    cubesidelength = float(input("Type Side Length of Cube: "))
    print(" ")
    print("Volume of Cube = ")
    print(cubesidelength*cubesidelength*cubesidelength)


if UserShape == "Rectangle":
    rectanglesidelength = float(input("Type Length of Rectangle: "))
    rectanglesidewidth = float(input("Type Width of Rectangle: "))
    print(" ")
    print("Area of Rectangle = ")
    print(rectanglesidelength*rectanglesidewidth)


if UserShape == "Rectangular Prism":
    rectangularprismsidelength = float(input("Type Length of Rectangle: "))
    rectangularprismsidewidth = float(input("Type Width of Rectangle: "))
    rectangularprismsideheight = float(input("Type Height of Rectangle: "))
    print(" ")
    print("Volume of Rectangular Prism = ")
    print(rectangularprismsidelength*rectangularprismsidewidth*rectangularprismsideheight)


if UserShape == "Triangle":
    trianglebase = float(input("Type Value of Triangle Base: "))
    triangleheight = float(input("Type Height of Triangle: "))
    print(" ")
    print("Area of Triangle = ")
    print(trianglebase*triangleheight/2)


if UserShape == "Triangular Prism":
    triangularprismbase = float(input("Type Value of Triangle Base on the Triangle Face Side: "))
    triangularprismheight = float(input("Type Height of Triangular Prism on Triangle Face Side: "))
    triangularprismaltitude = float(input("Type Altitude of Triangular Prism: "))
    print(" ")
    print("Volume of Triangular Prism = ")
    print(triangularprismbase*triangularprismheight/2*triangularprismaltitude)


if UserShape == "Pythagorean Theorem":
    import math
    from math import sqrt
    Therom = input("Choose The Side To Figure Out: A or B or C: ")
    print(" ")
    if Therom == "C":
        Ac = float(input("Type Value of A: "))
        Bc = float(input("Type Value of B: "))
        Csquared = ((Ac**2) + (Bc**2))
        print(" ")
        print("Value of C = ")
        print(sqrt(Csquared))
    if Therom == "B":
        Ab = float(input("Type Value of A: "))
        Cb = float(input("Type Value of C: "))
        Bsquared = ((Cb**2) - (Ab**2))
        print(" ")
        print("Value of B = ")
        print (sqrt(Bsquared))
    if Therom == "A":
        Ba = float(input("Type Value of B: "))
        Ca = float(input("Type Value of C: "))
        Asquared = ((Ca**2) - (Ba**2))
        print(" ")
        print("Value of A = ")
        print(sqrt(Asquared))



if UserShape == "Circle":
    import math
    circleradius = float(input("Type Radius of Circle: "))
    print(" ")
    print("Area of Circle = ")
    print((math.pi) * (circleradius**2))


if UserShape == "Sphere":
    import math
    sphereradius = float(input("Type Radius of Sphere: "))
    print(" ")
    print("Volume of Sphere = ")
    print((4 * math.pi) * (sphereradius**2))


print(" ")
print(" ")
print(" ")
