def is_prefect_number ( num ):
    if num <= 1 :
        return False
    sum_ = 0
    temp = num
    for i in range ( 1 , temp ):
        if  temp % i == 0 :
            sum_ += i

    return sum_ == num


try:
    number = int ( input ( "Enter the number to check for Perfect Number : ") )

    if is_prefect_number( number ):
        print ( f"{number} is a Perfect Number")
    else :
        print ( f"{number} is not a Perfect Number")

except ValueError:
    print ( "Please enter a valid integer.")