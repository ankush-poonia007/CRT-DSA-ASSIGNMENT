number = int ( input ( "Enter the nnumber : " ) )
digit = 0
print ( f" The reverse of {number} is : ")
while ( number > 0 ):
    digit = digit * 10 + number % 10
    number = number // 10

print(digit)