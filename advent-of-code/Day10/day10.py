with open("day10jolts.txt", 'r') as file:
    lines = list(file.readlines())

jolts = [0] #Stores each joltage level, but contains 0 (the joltage of the node at the start of the chain)

#Strip and parse lines, then add them to the jolts
for line in lines:
    line = int(line.strip('\n'))
    jolts.append(line)

#Sort jolts and add the adaptor rating
jolts.sort()
jolts.append(jolts[-1] + 3)

#Variables track the number of differences of 1, and differences of 3
one_count = 0
three_count = 0

#Iterate through jolts and find areas where the difference is 1 or 3
for x in range(len(jolts) - 1):

    if jolts[x+1] - jolts[x] == 1:
        one_count += 1
    elif jolts[x+1] - jolts[x] == 3:
        three_count += 1

print(f"Product: {one_count * three_count}") #Output result
