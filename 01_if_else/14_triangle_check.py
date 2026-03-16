# Program to check whether triangle is valid based on angles
print("Enter Three Angles of Triangle:")
angle1 = int(input())
angle2 = int(input())
angle3 = int(input())

# In Python, we can use a simple if-else or a ternary operator
if (angle1 + angle2 + angle3) == 180:
    print("Triangle is Valid")
else:
    print("Triangle is not Valid")