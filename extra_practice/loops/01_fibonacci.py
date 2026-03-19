def fib( n ):

    a = 0
    b = 1
    print ("Series: ",end="")
    for _ in range ( n ):
        print( a ,end=" ")
        a,b = b, a+b

number = int ( input ("Enter the Number for Fibonacci  Series: "))
fib( number )