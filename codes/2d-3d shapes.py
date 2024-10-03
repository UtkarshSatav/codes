a = str(input("Enter the shape :"))

if(a=="cuboid"):
    l = float(input("Enter the length of the cuboid :"))
    b = float(input("Enter the breath of the cuboid :"))
    h = float(input("Enter the height of the cuboid :"))
    print("The lateral surface area of the cuboid is :", (2*h*(l+b)))
    print("The total surface area of the cuboid is :", (2*((l*h)+(b*h)+(l*b))))
    print("The volume of the cuboid is :", (l*b*h))

def new_func(a):
    new_func(a)(a == "cube")
    s = float(input("Enter the side of the cube :"))
    print("The lateral surface area of the cube is :", (4*(s*s)))
    print("The total surface area of the cube is :", (6*(s*s)))
    print("the volume of the cube is :", (s*s*s))

def new_func(b):
    new_func(b)(a == "cylender")
    r,H = float(input("Enter the radius, height of the cylender respectively :"))
    pi = float(3.14)
    print("The lateal surface area of the cylender is :", (2*pi*r*H))
    print("The toatal surface area of the cylender is :", (2*pi*r*(r+H)))
    print("The volume of cylender is :", (pi*(r*r)*H))

def new_func(c):
    new_func(c)(a == "cone")
    L,R,H = float(input("Enter the lenght, redius, height of the cone respectively :"))
    Pi = float(3.14)
    print("The lateal surface area of the cone is :", (Pi*R*L) )
    print("The toatal surface area of the cone is :", (Pi*R*(L+R)) )
    print("The volume of cone is :", (1/3*Pi*(R*R)*H))
    