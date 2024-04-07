with open("day9numbers.txt", 'r') as file:
    numbers = [] #Array stores all numbers read from file

    for line in file:
        numbers.append(int(line))

valid = True #Variable stores value validity
start_index = 0 #Number tracks how many iterations have occurred, and where in the array to start the 25-item slice

#Continue loop as long as the latest number is valid
while valid:
    number = numbers[start_index + 25] #Number (26 + iteration count) in the array
    valid = False #Variable is false until loop confirms that the number is valid

    for x in numbers[start_index: start_index+25]: #Number 1 iterates through the sliced first 25 numbers
        for y in numbers[start_index: start_index+25]: #Number 2 iterates through the sliced first 25 numbers
            if x+y == number and x != y: #If there are two discrete numbers that sum up to the last value in the slice, then it is valid
                valid = True
                break

    start_index += 1 #Increment start index

sum_numbers = numbers[:start_index+24] #Slice includes all values before the first invalid number

#ALGORITHM: Iterate from two ends of the array. If the array closed by the boundaries of the two values sums up to the number, that sliced array is the solution

for x in range(len(sum_numbers)): #Iterator 1 (from the left)
    for y in range(len(sum_numbers)): #Iterate 2 (from the right)

        if sum(sum_numbers[x:len(sum_numbers)-y]) == number and x != y: #Check that the sliced array sums up to the total; make sure the boundaries aren't the same point

            sorted_arr = sum_numbers[x:len(sum_numbers)-y]
            sorted_arr.sort() #Sort array from highest to lowest (initial order does not matter, but this makes it easy to access the highest and lowest values)

            print(f"First Invalid Number: {number}")
            print(f"Sum of highest and lowest terms in the contiguous series that adds up to number: {sorted_arr[0] + sorted_arr[len(sorted_arr) - 1]}") #Output result
            break #Solution reached, exit loop
