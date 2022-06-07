mynumbers=[6,9,32,28,15,22,3,18]
minimum = mynumbers[0]

for x in mynumbers:
    if minimum > x:
      minimum = x
    maximum= mynumbers[0]

for x in mynumbers:
    if maximum < x:
     maximum = x
    average = 0

for x in mynumbers:
    average = average + x
average = average / len (mynumbers)

print("Minimum is: ")
print (minimum)
print("Maximum is: ")
print (maximum)
print("Average is: ")
print (average)
