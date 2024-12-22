# pattern_drawing.py

# Prompt the user to input the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize a counter for the while loop
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print asterisks side by side
    for _ in range(size):
        print("*", end="")  # Print asterisk without advancing to the next line
    print()  # Move to the next line after each row
    row += 1
