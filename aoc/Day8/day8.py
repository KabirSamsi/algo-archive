with open("bootcode.txt", 'r') as file:
    accumulated = 0 #Store accumulated values
    commands = [] #Matrix of each command and its distance
    executed = set() #Executed commands (use set to ensure no repeated values, and to improve search speed)

    #Read through file and parse into into commands matrix
    for line in file:
        commands.append((line.split()[0], int(line.split()[1]))) #Append tuple to matrix

counter = 0 #Counter tracks which command is being executed

#Iterate through commands
while counter < len(commands):

    if counter in executed: #If repeating instruction, terminate loop
        break
    else:
        executed.add(counter) #Add this command index to executed set

        #Depending on command, modify accumulated and/or counter
        if commands[counter][0] == 'nop':
            counter += 1
        elif commands[counter][0] == 'acc':
            accumulated += commands[counter][1]
            counter += 1
        elif commands[counter][0] == 'jmp':
            counter += commands[counter][1]

print(f"Total Accumulated: {accumulated}") #Output results
