import random
list=["McDonalds", "In N Out", "Burger King"]
num1 = ["Big Mac", "McNuggets", "Fries", "Quarter Pounder"]
num2 = ["Double Double", "Fries", "Shake", "Triple Triple"]
num3 = ["Whopper", "Chicken Fries", "Fries", "Spicy Chicken Sandwhich"]

y = random.randrange(0,4)
x = input("Which restaurant? ")
if x == "Mcdonalds":
    print (num1)
    print (num1[random.randrange(4)])
elif x == "In N Out":
    print (num2)
    print (num2[random.randrange(4)])
elif x == "Burger King":
    print (num3)
    print (num3[random.randrange(4)])
else:
    print("Try Again")

