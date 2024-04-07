#Dictionary of eigenvectors for translating in each direction (stretch dependent on how many units to move in a given direction)
TRANSLATION_VECTORS = {
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
    "N": (0, 1)
}

ORIENTATIONS = ('E', 'S', 'W', 'N') #Different ORIENTATIONS (can't be stored in dictionary, since order is important)

ORIENTATION_CHANGES = {'R': 1, 'L': -1} #Determines where the orientation changes to (where to iterate in ORIENTATIONS tuple)
orientation = 'E' #Stores current orientation

with open("day12directions.txt", 'r') as file:
    directions = [] #Stores all directions
    for line in file:
        directions.append((line[0], int(line[1:])))

position = [0, 0] #Starting position is at (0, 0)

for direction in directions:
    if direction[0] in TRANSLATION_VECTORS: #If the change is in a specific direction, vector operation translates position
        position[0] += (TRANSLATION_VECTORS[direction[0]][0] * direction[1])
        position[1] += (TRANSLATION_VECTORS[direction[0]][1] * direction[1])

    elif direction[0] == 'F': #If not in a specific direction (requires evaluation of current orientation), vector operation translates position with respect to orientation
        position[0] += (TRANSLATION_VECTORS[orientation][0] * direction[1])
        position[1] += (TRANSLATION_VECTORS[orientation][1] * direction[1])

    elif direction[0] in ORIENTATION_CHANGES: #Switching orientation
        pos_counter = ORIENTATIONS.index(orientation)
        for x in range(int(direction[1]/90)): #There exists a new specific direction (E, S, W, N) at each 90-degree turn
            pos_counter += ORIENTATION_CHANGES[direction[0]]

            #If end of array is reached on either end, return to the other end (works like unit circle)
            if pos_counter >= len(ORIENTATIONS):
                pos_counter = 0
            elif pos_counter < 0:
                pos_counter = len(ORIENTATIONS) - 1
            orientation = ORIENTATIONS[pos_counter] #Set new orientation to equal the translated orientation

print(f"Manhattan Distance: {abs(position[0]) + abs(position[1])}") #Output results
