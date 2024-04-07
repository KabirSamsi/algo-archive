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

print(f"First Invalid Number: {number}") #Output result
