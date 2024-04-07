#Dictionary of eigenvectors for translating in each direction (stretch dependent on how many units to move in a given direction)
TRANSLATION_VECTORS = {
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
    "N": (0, 1)
}

ORIENTATION_CHANGES = {'R': 1, 'L': -1} #Determines where the orientation changes to (where to iterate in ORIENTATIONS tuple)

with open("day12directions.txt", 'r') as file:
    directions = [] #Stores all directions
    for line in file:
        directions.append((line[0], int(line[1:])))

position = [0, 0] #Starting position is at (0, 0)
waypoint = [10, 1] #Waypoint vector starts at (10, 1)

for direction in directions:

    if direction[0] in TRANSLATION_VECTORS: #If the change is in a specific direction, vector operation translates position
        waypoint[0] += (TRANSLATION_VECTORS[direction[0]][0] * direction[1])
        waypoint[1] += (TRANSLATION_VECTORS[direction[0]][1] * direction[1])

    elif direction[0] == 'F': #If not in a specific direction (requires evaluation of current orientation), vector operation translates position with respect to orientation
        distance_vector = [waypoint[0]*direction[1], waypoint[1]*direction[1]] #Multiplies distance between ship and waypoint by given scalar
        position[0] += distance_vector[0]
        position[1] += distance_vector[1]

    elif direction[0] in ORIENTATION_CHANGES: #Switching orientation
        if direction[0] == 'R': #Clockwise/counterclockwise motion works in 360 degree circle. To change a rotation's direction, subtract it from 360
            degree_change = 360 - direction[1]
        else:
            degree_change = direction[1]

        for x in range(int(degree_change/90)): #Number of 90 degree rotations (all the listed rotations are multiples of 90)
            waypoint = [waypoint[1]*-1, waypoint[0]] #Rotation vector [-y, x] rotates the waypoint vector

print(f"Manhattan Distance: {abs(position[0]) + abs(position[1])}") #Output results
