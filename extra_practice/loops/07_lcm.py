def hcf(num1,num2):
    while True:
        rem = 0
        if num1 > num2 :
            rem = num1 % num2
            if rem :
                num1 = num2
                num2 = rem
            else:
                return num2
        else:
            num1,num2 = num2,num1
def hcf_lcm_calculator():
    menu = {
        1:"HCF",
        2:"LCM",
        3:"END"
    }



    while True:

        print(f"Select Menu")
        print(f"Menu : {menu}\nSelect 1 For {menu[1]}\nSelect 2 For {menu[2]}")
        choice = int(input("Enter Your Choice: "))


        match choice:

            case 1:
                n1 = int(input("Enter the First Number"))
                n2 = int(input("Enter the Second Number"))
                HCF = hcf( n1 , n2 )
                print(f"HCF : {HCF}")



            case 2:
                n1 = int(input("Enter the First Number"))
                n2 = int(input("Enter the Second Number"))

                HCF = hcf(n1, n2)
                LCM = (n1 * n2) // HCF

                print(f"LCM of Number {n1} and {n2} is : {LCM}")

            case 3 :
                print("Program Ended !!")
                break
            case _:
                print("Invalid Choice !!")




options = {
    1:"Continue",
    2:"Discontinue"
}

# And update the print below it too
print(f"Select Menu\n{1}: {options[1]}\n{2}: {options[2]}")
ch = int(input("Enter Your Choice: "))
if ch == 1:
    hcf_lcm_calculator()
print("Thank You!!")