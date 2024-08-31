#Arithmatic operators

a = 5
b = 2

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) #reaminder
print(a**b) #a^b

#Relational operaations

a=50
b=20

print(a==b) #False
print(a!=b) #True
print(a>=b) #True
print(a>b)  #True
print(a<=b) #False
print(a<b)  #False

#Assignment operator

num = 10
num += 10  #10 +10 => 20  #You can put all arithmatic operation "+=,-=,*=,/=,%=,**="

print(" num = ", num)

#logical operator

#NOT    # not gives you the opposite value "false = true , true = false
a = 50
b = 20

print (not (a>b))     
print (not (a<b))

#AND    # and gives you the value of a and b "if a=true and b=true then value is true but if one is false then its false"
val1 = True   
val2 = False

print("And operator : ",val1 and val2)

print("Or operator : ", val1 or val2) #OR    # or gives you the value of a and b "if a=true and b=false then still the value is true "

# Type conversion

a = int("2")  # int , float 
b = 2.14

print(type(a))
print(a+b)

a = 2.14
a = str(a)

print(type(a))