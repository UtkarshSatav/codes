a = int(input("enter your first value :"))
b = int(input("enter your second value :"))
c = int(input("enter your third value :"))

if(a >= b and a >= c):
    print("the greatest no. is :",a)

elif(b >= c):
    print("the greatest no. is :",b)

else:
    print("the greatest no. is :",c)