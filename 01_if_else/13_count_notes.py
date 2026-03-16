# Program to count total number of notes in given amount
amount = int(input("Enter the Amount: "))

# Define note denominations
denominations = [500, 100, 50, 20, 10, 5, 2, 1]

print("Total Number of Notes")
for note in denominations:
    count = amount // note  # Calculate how many notes of this value
    amount %= note         # Remaining amount after taking those notes
    print(f"{note} = {count}")