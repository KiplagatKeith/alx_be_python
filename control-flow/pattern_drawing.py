# Prompt user for input
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# While loop for rows
while row < size:
    # For loop for columns (printing stars in a row)
    for col in range(size):
        print("*", end="")  # stay on same line
    print()  # move to next line after finishing a row
    row += 1
