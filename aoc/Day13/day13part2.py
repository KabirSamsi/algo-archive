#Super useful theorem for evaluating an unknown number based on the remainders when dividing it by smaller numbers (A variant of the premise of this problem.)
#See my notes in chinese_remainder_theorem.py and the attached links to learn more!

from chinese_remainder_theorem import chinese_remainder_theorem

with open("day13buses.txt", 'r') as file:
    data = [] #Data from file
    for line in file:
        data.append(line)

    buses = [] #Array keeps track of each bus

    for segment in data[1].split(','): #Add buses listed in second line of file to array
        if segment != 'x':
            buses.append(int(segment))
        else:
            buses.append(1) #Any integer divisible by 1, so no constraints

    buses = sorted(enumerate(buses), key=lambda x:x[1]) #Sorts buses using anonymous function and inbuilt functions, but stores original order in tuple-dict like format

    switched_buses = []
    for bus in buses: #Remove any 'x' values
        if bus[1] != 1:
            switched_buses.append(list(bus)[::-1]) #Reverse the bus so that the remainder is the second term (more aesthetically visual)

    buses = switched_buses[:]
    switched_buses = []

    for bus in buses: #Multiply each remainder by -1 (since every new value has to be divisible by 1+starting value, each remainder is technically negative)
        switched_buses.append((bus[0], bus[1]*-1))
    buses = switched_buses[:]

    result = chinese_remainder_theorem(buses) #Perform Chinese Remainder Theorem function

    print(f"First valid timestamp: {result}") #Output result (to get the initial starting value, subtract the increment factor from the final value)
