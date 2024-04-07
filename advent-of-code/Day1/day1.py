with open("day1entries.txt", "r") as file:
    entries = []
    for line in file:
        entries.append(int(line))

#Variables to track the two correct numbers, and their product
num1 = 0
num2 = 0
product = 0

#Track 2 numbers in the list of numbers, by index
for x in range(len(entries)):
    for y in range(len(entries)):

        #Evaluate sum and make sure entry indices are not the same
        if entries[x]+entries[y] == 2020 and x != y:
            num1 = entries[x]
            num2 = entries[y]
            product = entries[x]*entries[y]
            break

#Output results
print(f"Number 1: {num1}")
print(f"Number 2: {num2}")
print(f"Product: {product}")
