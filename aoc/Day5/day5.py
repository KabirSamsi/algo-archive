#Math and stats libraries will be used later for rounding and mean calculations
import math
import statistics
from day5seat import Seat

with open("day5positions.txt", 'r') as file:
    seats = [] #Array will store Seat objects

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

        #Create Seat object and add it to array
        seat = Seat(line.split('\n')[0], row_range[0], col_range[0])
        seats.append(seat)

highest = seats[0] #Temporary seat with highest ID (will change with iterations)

#Iterate over seats to find the one with highest ID
for seat in seats:
    if seat.id > highest.id:
        highest = seat

print(f"Seat with the highest ID - {highest.code}: row {highest.row}, column {highest.col}, seat ID {highest.id}") #Output results
