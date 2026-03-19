num1 = int ( input ( "Enter the First Number" ) )
num2 = int ( input ( "Enter the Second Number" ) )

while True:
    rem = 0
    if num1 > num2 :
        rem = num1 % num2
        if rem :
            num1 = num2
            num2 = rem
        else:
            print("HCF is ",num2)
            break
    else:
        num1,num2 = num2,num1