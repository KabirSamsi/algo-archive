with open("day17grid.txt", 'r') as file:
    position_vectors = [] #Position vectors track the 26 possible movements
    position_changes = [-1, 0, 1]
    for x in position_changes:
        for y in position_changes:
            for z in position_changes:
                if (x, y, z) != (0, 0, 0): #Stationary motion should not be possible
                    position_vectors.append((x, y, z))

    pocket_dimension = [] #Pocket Dimension Matrix

    #Build the input as 1 slice of the pocket dimension and add it
    slice = []
    for line in file:
        slice.append(line.rstrip('\n'))
    pocket_dimension.append(slice)

    for x in range(6): #Perform operation 6 times

        #THIS SECTION ADDS INACTIVE SIDES TO EACH DIMENSION
        new_dimension = [] #Builds dimension with edits based on pocket dimension
        for slice in pocket_dimension:
            new_slice = []
            for row in slice: #Build a new row with new empty columns at either side
                new_row = '.' + row + '.'
                new_slice.append(new_row)

            #Build new slice with empty rows at either side
            new_slice.insert(0, '.'*len(new_slice[0]))
            new_slice.insert(len(new_slice), '.'*len(new_slice[0]))
            new_dimension.append(new_slice)

        #Build new slice based on the number of rows in each other slice, and add it to pocket dimension
        new_slice = []
        for row in new_dimension[0]:
            new_slice.append('.'*len(row))
        new_dimension.insert(0, new_slice)
        new_dimension.insert(len(new_dimension), new_slice)
        pocket_dimension = new_dimension[:] #Make pocket dimension equal the new modified dimension

        #THIS SECTION EVALUATES AND MODIFIES POCKET DIMENSION
        new_dimension = [] #Once again, new dimension is an empty matrix

        for s in range(len(pocket_dimension)): #Iterate through each slice
            new_dimension.append([]) #Add an empty row
            for r in range(len(pocket_dimension[s])): #Iterate through each row
                new_colset = "" #Create a new string to store each column

                for c in range(len(pocket_dimension[s][r])):
                    neighbor_count = 0 #Counts the number of active neighbors
                    for vector in position_vectors: #Check the character at each position vector
                        if (s+vector[0] in range(len(pocket_dimension))) and (r+vector[1] in range(len(pocket_dimension[s]))) and (c+vector[2] in range(len(pocket_dimension[s][r]))): #Removes any chance of index error
                            if pocket_dimension[s+vector[0]][r+vector[1]][c+vector[2]] == '#': #If this particular position is active, increment neighbor count
                                neighbor_count += 1

                    #Build new dimension based on rules provided in problem
                    if pocket_dimension[s][r][c] == '.':
                        if neighbor_count == 3:
                            new_colset += '#'
                        else:
                            new_colset += '.'

                    elif pocket_dimension[s][r][c] == '#':
                        if neighbor_count in (2, 3):
                            new_colset += '#'
                        else:
                            new_colset += '.'
                new_dimension[s].append(new_colset)

        pocket_dimension = new_dimension[:] #Set original pocket dimension to equal the new one

    #Count total active cubes
    total_active = 0
    for z in range(len(pocket_dimension)):
        for row in pocket_dimension[z]:
            total_active += row.count('#')

    print(f"Total Active Cubes After 6 cycles: {total_active}") #Output result
