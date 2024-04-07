from bytify import convert_to_bytes, debin #Import functions

with open('day14bytes.txt', 'r') as file:
    mask = '' #Bitmask will store the constantly changing mask through file iteration
    memory = {} #Stores each memory block (dictionary form prevents need for a value at every index)

    for line in file:
        if line[:4] == 'mask': #If the command is to change the mask
            mask = line.split('= ')[1] #Modify mask based on command

        elif line[:3] == 'mem': #If the command is to change the memory
            memory[line.split('[')[1].split(']')[0]] = debin(convert_to_bytes(int(line.split('= ')[1]), mask)) #Modify the memory position listed using functions in bytify.py file

    #Iterate through memory dictionary and add up values
    val_sum = 0
    for bit in memory:
        val_sum += memory[bit]

    print(f"Sum of Memory Values: {val_sum}") #Output result
