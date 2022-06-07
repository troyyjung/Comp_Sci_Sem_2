x= int(input("Please enter your first number: "))
y= (input("Please enter an opertation:  "))
z= int(input("Please enter your second number: "))
if y== "+":
    print(x+z)
elif y== "-":
    print (x-z)
elif y== "*":
    print(x*z)
elif y== "/":
    print(x/z)
else:
    print("invalid, try again")