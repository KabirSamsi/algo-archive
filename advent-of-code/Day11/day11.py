POSITION_VECTORS = ((0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1)) #Position vectors track the eight possible adjacent seats
seats = [] #Matrix stores arrangement after each iteration (used as previous matrix which arrangement matrix is based on)
arrangement  = [] #Matrix is built durinng iteration based on vector operations on initial 'seats' matrix

with open("day11seats.txt", 'r') as file:
    for line in file:
        seats.append(list(line.rstrip('\n')))

while seats != arrangement: #While the previous matrix is not the new one (while the seats are still changing)

    if len(arrangement) > 0: #Don't change on the start round (when the arrangement is still empty)
        seats = arrangement #Prepare to change the matrix, so set the previous one to equal the current one
        arrangement =  []

    for x in range(len(seats)): #Iterate through each row in the matrix
        arrangement.append([]) #Add an empty row (will be filled out in following operations)
        for y in range(len(seats[x])): #Iterate through each item in row

            if seats[x][y] == '.': #Nothing happens if the seat is floor ('.')
                arrangement[x].append('.')

            elif seats[x][y] == 'L': #Operations if the seat is empty
                available = True #Tracks seat availability
                for vector in POSITION_VECTORS: #Perform each vector operation in the tuple of vectors
                    if ((x+vector[0]) in range(len(seats))) and ((y+vector[1]) in range(len(seats[x]))): #Remove any chance of index error from vector operations
                        if seats[x+vector[0]][y+vector[1]] not in ('L', '.'): #If seat is occupied
                            available = False #If any seat breaks the adjacency rule, seat is not available
                            break
                if available: #If the seat is available, occupy it. Otherwise, it remains the same
                    arrangement[x].append('#')
                else:
                    arrangement[x].append('L')

            elif seats[x][y] == '#': #Operations if the seat is occupied
                occupied_count = 0 #Tracks how many seats are occupied
                for vector in POSITION_VECTORS: # Perform each vector operation in the tuple of vectors
                    if ((x+vector[0]) in range(len(seats))) and ((y+vector[1]) in range(len(seats[x]))): #Remove any chance of index error from vector operations
                        if seats[x+vector[0]][y+vector[1]] == '#': #Each vector translation maps onto an adjacent seat. If that seat is occupied, occupied_count increments
                            occupied_count += 1
                if occupied_count >= 4: #Given condition - if 4+ adjacent seats are occupied, this seat becomes empty
                    arrangement[x].append('L')
                else:
                    arrangement[x].append('#')

total_occupied = 0
print("\nFinal Arrangement: ")
for row in arrangement: #Print out final arrangement
    print(''.join(row))
    total_occupied += row.count('#') #Track how many seats are occupied

print(f"\nTotal Seats Occupied: {total_occupied}") #output result
