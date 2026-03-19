limit = int ( input ( "Enter the limiting Number between 1 and 100" ) )
sum = 0
for i in range ( 1,limit + 1 ):

    if i % 2 == 0 :
        sum += i

print ( f"Sum from 1 till {limit} in between 100  is {sum}")