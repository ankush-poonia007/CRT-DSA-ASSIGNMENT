limit = int ( input ( "Enter the limiting Number between 1 and 100" ) )

for i in range ( 1,limit + 1 ):
    if i % 2 == 0:
        print ( i )