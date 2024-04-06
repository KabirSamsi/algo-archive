import math #Math module will be used for rounding operations

with open("day3trees.txt", 'r') as file:
    lines = [] #File array contains each line from file (so file doesn't have to be reopended and reread each time)
    for line in file: #Add values from file to file array
        lines.append(line)

slope = [] #Slope matrix stores info about the trees and open spots on the 'slope'
line_count = len(lines) #Number of lines in the file

#For every line in the file, add 3 of the line to the file
for line in lines:
    slope.append(line[0:-1] * (len(line) * (math.ceil(line_count / len(line)) * 3))) #Need to traverse right three for every traversal down 1 => rows must be 3x as long as cols

tree_count = 0 #Store how many trees are there
row = 0
col = 0

while (row < len(slope) - 1):
    #Move 3 to the right and 1 down
    row += 1
    col += 3

    #At every iteration, increment by 3 for columns and 1 for rows
    if slope[row][col] == '#':
        tree_count += 1

print(f"Tree Count: {tree_count}") #Output final result
