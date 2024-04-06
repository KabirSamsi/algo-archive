#Implements a similar tree-like structure from bottom-top like Version 1, but does so through reversing an array. More memory-efficient

lines = open("../day10jolts.txt").read().rstrip().split('\n')

jolts = list(map(int, lines)) #Make a list of jolts as integer values

#Sort, add 0 to the start, and add the highest value + 3 to the end
jolts.append(0)
jolts.sort()
jolts.append(jolts[-1] + 3)

succeeding_jolts = {} #Dict maps each jolt to its possible succeeding values
jolts.reverse() #Reversing jolts (this way, program calculates possible sequences from the end and builds the tree from highest value (only 1 possible path) to 0 (all paths))

#Enumerate allows program to access each value as key-value "index-item" pairs
for index, jolt in enumerate(jolts):
    next_jolt_arr = jolts[:index][-3:] #Add the three values next to this value (the three next successive terms, algorithm next evaluates to see if they fall in the 0 < x < 3 range)

    if len(next_jolt_arr) <= 0: #(For final array) if no terms beyond this value exist,
        succeeding_jolts[jolt] = 1 #Set the number of arrangements from this point to 1 (sequence must terminate right now, there are no other possible arrangements)
        continue #Continue loop

    succeeding_jolts[jolt] = 0 #Start each sequence with 0 possible arrangements
    for j in next_jolt_arr: #Iterate through the next possible values
        if j - jolt in range(1, 4): #If there is a 1-3 gap in between values (meaning this value is valid)
            succeeding_jolts[jolt] += succeeding_jolts[j] #The number of possible sequences from this point is equal to the sum of possible sequences for all its next nodes (implements the tree structure)

print(f"Total Combinations: {succeeding_jolts[0]}") #Output result for the dict at value 0 (the lowest value, which will have all possible arrangements)
