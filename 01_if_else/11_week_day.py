# Program to input week number and print week day
choice = int(input("Enter the Week Number(1-7) : "))

# Dictionary mapping for week days
days = {
    1: "Sunday",
    2: "Monday",
    3: "Tuesday",
    4: "Wednesday",
    5: "Thursday",
    6: "Friday",
    7: "Saturday"
}

# Use .get() to provide a default message if the key isn't found
print(days.get(choice, "Enter a Valid Choice"))