
rows = int(input("Enter the size of the pattern: "))

i = 0  
while i < rows:
    for star in range(rows):
        print("*", end="")  
    print() 
    i += 1  # Move to the next row
