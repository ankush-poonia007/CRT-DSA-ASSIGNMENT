choice = int(input("Enter the Week Number(1-7) : "))

# Python doesn't have a traditional 'switch'.
# We use if/elif or a dictionary.
days = {
    1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday",
    5: "Thursday", 6: "Friday", 7: "Saturday"
}

print(f"This is {days.get(choice, 'an Invalid Choice')}")