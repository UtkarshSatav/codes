# Cuboid 
a = str(input("Enter the shape you :"))

if(a == "cuboid"):
    l = float(input("Enter the length of the cuboid :"))
b = float(input("Enter the breath of the cuboid :"))
h = float(input("Enter the height of the cuboid :"))
print("The lateral surface area of the cuboid is :", (2*h*(l+b)))
print("The total surface area of the cuboid is :", (2*((l*h)+(b*h)+(l*b))))
print("The volume of the cuboid is :", (l*b*h))

if(a == "cube"): 
    s = float(input("Enter the side of the cube :"))
print("The lateral surface area of the cube is :", (4*(s*s)))
print("The total surface area of the cube is :", (6*(s*s)))
print("the volume of the cube is :", (s*s*s))

if(a == "cylender"):
    r = float(input("Enter the radius of the cylender :"))
H = float(input("Enter the height of the cylender :"))
pi = float(3.14)
print("The lateal surface area of the cylender is :", (2*pi*r*H))
print("The toatal surface area of the cylender is :", (2*pi*r*(r+H)))
print("The volume of cylender is :", (pi*(r*r)*H))

