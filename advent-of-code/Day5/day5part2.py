#Math and stats libraries will be used later for rounding and mean calculations
import math
import statistics

with open("day5positions.txt", 'r') as file:

    seatIds = [] #Array will store seat Ids (no need for objects, because only tracking ID)

    for line in file:
        row_range = [0, 127] #The current range of rows. With each iterated operation, the list gets smaller and tends towards one number

        for row_pos in line[0:7]: #Row Position iterates over the first 7 terms (the 'F' and 'B' terms that determine row position)
            if row_pos == 'F':
                row_range = [row_range[0], math.floor(statistics.mean(row_range))] #If to the front, take only the lower part of the array

            elif row_pos == 'B':
                row_range = [math.ceil(statistics.mean(row_range)), row_range[1]] #If to the back, take only the upper part of the array


        col_range = [0, 7] #The current range of seat columns. With each iterated operation, the list gets smaller and tends towards one number

        for col_pos in line[7:]: #Column Position iterates over the last 3 terms (the 'L' and 'R' terms that determine column position)

            if col_pos == 'L':
                col_range = [col_range[0], math.floor(statistics.mean(col_range))] #If to the left, take only the lower part of the array

            elif col_pos == 'R':
                col_range = [math.ceil(statistics.mean(col_range)), col_range[1]] #If to the right, take only the upper part of the array

        #Add ID to array
        seatIds.append((row_range[0] * 8) + col_range[0])

seatIds.sort() #Sort array from least to greatest
seatID = 0 #Temporary seat ID (will change with iterations)

#Iterate through sorted list. If, ay any point, there is a gap between IDS of more than 1, that point is my seat.
for x in range(len(seatIds)-1):
    if (seatIds[x+1] - seatIds[x] != 1):
        seatID = seatIds[x] + 1

print(f"My seat ID: {seatID}") #Output results
