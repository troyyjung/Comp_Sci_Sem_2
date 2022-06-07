x=int(input("Please enter line length: "))
y=input("Vertical or Horizontal line: ")

if y== "Vertical":
    for c in range(0,x):
        print("*")
        
elif y == "Horizontal":
    for a in range (0,x):
        print("*", end = "")