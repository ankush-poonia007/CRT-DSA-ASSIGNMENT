number = int ( input ( "Enter the nnumber : " ) )
digit = 0
print ( f"The sum of {number} is : ",end="")
while ( number > 0 ):
    digit += number % 10
    number = number // 10

print(digit)