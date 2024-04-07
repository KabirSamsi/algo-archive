from bytify import convert_to_bytes2, debin2 #Import functions

with open('day14bytes.txt', 'r') as file:
    mask = '' #Bitmask will store the constantly changing mask through file iteration
    memory = {} #Stores each memory block (dictionary form prevents need for a value at every index)

    for line in file:
        if line[:4] == 'mask': #If the command is to change the mask
            mask = line.split('= ')[1] #Modify mask based on command

        elif line[:3] == 'mem': #If the command is to change the memory
            positions = debin2(convert_to_bytes2(int(line.split('[')[1].split(']')[0]), mask)) #Use functions from binary conversion/bytify file to get all the positions

            for pos in positions: #Iterate through positions and set each one to equal the given value
                memory[pos] = int(line.split('= ')[1])

    #Iterate through memory dictionary and add up values
    val_sum = 0
    for bit in memory:
        val_sum += memory[bit]

    print(f"Sum of Memory Values: {val_sum}") #Output result
