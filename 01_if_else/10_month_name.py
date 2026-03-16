choice = int(input("Enter the Month Number(1-12) : "))

months = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}

if 1 <= choice <= 12:
    print(f"This is {months[choice]}")
else:
    print("Enter a Valid Choice")