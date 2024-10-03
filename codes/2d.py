a = str(input("Enter the 2d shape :"))
pi = float(3.14)
X =["square","rectangle","circle","trianglr"]

if(a=="square"):
    side=float(input("Enter the side of the square :"))
    print("The area of the square is :", (side*side))
    print("The peremeter of the square is :", (4*side))

elif(a=="rectangle"):
    length = float(input("Enter the length of the rectangle :"))
    wreath = float(input("Enter the wreath of the rectanglr"))
    print("The area of the rectangle is :", (length*wreath))
    print("The peremeter of the rectangle is :", (2*(length+wreath)))

elif(a=="triangle"):
    s1,s2,s3 = float(input("Enter the 3 sides of the triangle respectively :"))
    h = float(input("Enter the height of the triangle :"))
    print("The area of the triangle is :", ((s2*h)/2))
    print("The peremiter of the teiangle is :",(s1+s2+s3))

elif(a=="circle"):
    r = float(input("Enter the radius of the circle :"))
    print("The area of the circle is :", (pi*(r*r)))
    print("The peremeter of the circle is :", (2*pi*r))

else:
    print("The shape you have enter does not match any share from the program plz try a different shape")
    print("The shapes which are there in the program are :",X)