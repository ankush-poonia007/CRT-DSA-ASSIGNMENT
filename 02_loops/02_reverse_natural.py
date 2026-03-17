#16. Write a program to print all natural numbers in reverse


start = int ( input ( " Enter the starting number: "))
end = int ( input ( "Enter the enging Number : "))

for i in range ( end , start - 1 , -1 ):

    print ( i )