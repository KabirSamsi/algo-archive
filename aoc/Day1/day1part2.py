with open("day1entries.txt", "r") as file:
    entries = []
    for line in file:
        entries.append(int(line))

#Variables to track the three correct numbers, and their product
num1 = 0
num2 = 0
num3 = 0
product = 0

#Track 3 numbers in the list of numbers, by index
for x in range(len(entries)):
    for y in range(len(entries)):
        for z in range(len(entries)):

            #Evaluate sum and make sure entry indices are not the same
            if entries[x]+entries[y]+entries[z] == 2020 and x != y and x !=z  and y != z:
                num1 = entries[x]
                num2 = entries[y]
                num3 = entries[z]
                product = entries[x]*entries[y]*entries[z]
                break

#Output results
print(f"Number 1: {num1}")
print(f"Number 2: {num2}")
print(f"Number 3: {num3}")
print(f"Product: {product}")
