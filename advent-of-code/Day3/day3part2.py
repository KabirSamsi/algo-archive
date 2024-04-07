import math #Math module will be used for rounding operations

def count_trees(fileArr, col_inc, row_inc): #Function to count trees (based on the file of the slope, column increment (how much to move to the right) and row increment (how much to move down))
    slope = []
    line_count = len(fileArr) #Number of lines in the file

    for line in fileArr: #Create array of trees based on column increment (the amount moving to the right determines how many times to multiply each row)
        slope.append(line[0:len(line)-1] * (len(line) * (math.ceil(line_count / len(line)) * col_inc))) #Need to traverse right three for every traversal down 1 => rows must be 3x as long as cols

    #Keep track of tree count, row position, and column position
    tree_count = 0
    row = 0
    col = 0

    while (row < len(slope) - 1):

        #At every iteration, increment by the row increment for rows and column increment for columns
        row += row_inc
        col += col_inc

        #Evaluate whether a tree exists at that point, if so, add 1
        if slope[row][col] == '#':
            tree_count += 1

    return tree_count #Function return value is the number of trees calculated

with open("day3trees.txt", 'r') as file:
    fileArr = [] #File array contains each line from file (so file doesn't have to be reopended and reread each time)

    #Add values from file to file array
    for line in file:
        fileArr.append(line)

#Multiply each version to get the final product
product = count_trees(fileArr, 1, 1) * count_trees(fileArr, 3, 1) * count_trees(fileArr, 5, 1) * count_trees(fileArr, 7, 1) * count_trees(fileArr, 1, 2)

print(f"Product Of Tree Counts: {product}")
