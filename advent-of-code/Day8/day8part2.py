with open("bootcode.txt", 'r') as file:
    commands = [] #Matrix of each command and its distance

    #Read through file and parse into into commands matrix
    for line in file:
        commands.append([line.split()[0], int(line.split()[1])]) #Append list to matrix

switches = [] #Stores all the spots at which a command will be switched

#If command is "nop" or "jmp", it will be switched during the iteration process
for x in range(len(commands)):
    if commands[x][0] in ("nop", "jmp"):
        switches.append(x)

#Iterate through each switch and change the looping at that point
for switch in switches:
    counter = 0 #Counter tracks which command is being executed (refresh with each iteration)
    infinite = False #Track whether the loop is infinite, or can compile successfully (refresh with each iteration)
    accumulated = 0 #Store accumulated values (refresh with each iteration)
    executed = set() #Executed commands (use set to ensure no repeated values, and to improve search speed) (refresh with each iteration)

    #Iterate through commands
    while counter < len(commands):

        if counter in executed: #If repeating instruction, terminate loop
            infinite = True
            break
        else:
            executed.add(counter) #Add this command index to executed set

            #Depending on command, modify accumulated and/or counter
            if commands[counter][0] == 'nop':
                if counter == switch: #If this is the switch iteration, then perform "jmp" instead of "nop"
                    counter += commands[counter][1]
                else:
                    counter += 1

            elif commands[counter][0] == 'acc':
                accumulated += commands[counter][1]
                counter += 1

            elif commands[counter][0] == 'jmp':
                if counter == switch: #If this is the switch iteration, then perform "nop" instead of "jmp"
                    counter += 1
                else:
                    counter += commands[counter][1]

    if not infinite: #If the loop is able to compile successfully, then output result
        print(f"Total Accumulated After Successful Loop: {accumulated}")
        break #End switch iteration
