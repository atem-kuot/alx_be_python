rows = int(input("Enter the size of the pattern: "))

for i in range(rows):
    # Print stars
    for star in range(rows):
        print("*", end="")

    print()  # Move to the next line
