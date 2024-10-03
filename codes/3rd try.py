a = str(input("Enter the 3d shape :")) #3d objects 
pi = float(3.14)
y = ["cuboid","cube","cylender","cone","sphere","hemisphere"]
if(a=="cuboid"):
    l = float(input("Enter the length of the cuboid :"))
    b = float(input("Enter the breath of the cuboid :"))
    h = float(input("Enter the height of the cuboid :"))
    print("The lateral surface area of the cuboid is :", (2*h*(l+b)))
    print("The total surface area of the cuboid is :", (2*((l*h)+(b*h)+(l*b))))
    print("The volume of the cuboid is :", (l*b*h)) 

elif(a=="cube"):
    s = float(input("Enter the side of the cube :"))
    print("The lateral surface area of the cube is :", (4*(s*s)))
    print("The total surface area of the cube is :", (6*(s*s)))
    print("the volume of the cube is :", (s*s*s))

elif(a=="cylender"):
    r = float(input("Enter the radius of the cylender  :"))
    H = float(input("Enter the height of the cylender  :"))
    print("The lateal surface area of the cylender is :", (2*pi*r*H))
    print("The toatal surface area of the cylender is :", (2*pi*r*(r+H)))
    print("The volume of cylender is :", (pi*(r*r)*H))

elif(a=="cone"):
    L = float(input("Enter the lenght of the cone  :"))
    R = float(input("Enter the redius of the cone  :"))
    H = float(input("Enter the height of the cone  :"))
    print("The lateral surface area of the cone is :", (pi*R*L))
    print("The total surface area of the cone is :", (pi*R*(L+R)))
    print("The volume of the cone is :",(1/3*pi*(R*R)*H))

elif(a=="sphere"):
    A = float(input("Enter the redius of the sphere :"))
    print("The toatal surface area of the sphere is :", (4*pi*(A*A)))
    print("The volume of sphere is :", ((4/3)*pi*(A*A*A)))

elif(a=="hemisphere"):
    X = float(input("Enter the radius of the hemisphere :"))
    print("The lateal surface area of the hemisphere is :", (2*pi*(X*X)) )
    print("The toatal surface area of the hemisphere is :", (3*pi*(X*X)) )
    print("The volume of hemisphere is :", ((2/3)*pi*(X*X*X)))

else:
    print("The shape you have enter does not match any share from the program plz try a different shape")
    print("The shapes which are there in the program are :",y)