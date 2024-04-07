#Brute force algorithm. I went to the subreddit and surprisingly, there are no cleaner mathematical ways to solve this problem! Anybody have any better ideas on how to solve this?

numbers = [17,1,3,16,19,0] #Number input

count = len(numbers) #Stores how many iterations have occured (start with the number of items already in  array)

while count < 30000000:
    if numbers.count(numbers[-1]) > 1: #If there is more than 1 instance of the number
        positions = [] #Stores all the positions at which this number occurs

        for x in range(len(numbers)): #Iterate through numbers and find instances of this number
            if numbers[x] == numbers[-1]:
                positions.append(x)

        numbers.append(positions[-1]-positions[-2]) #Add the difference between the last two values

    else: #If there is only one instance of the number, add 0
        numbers.append(0)

    count += 1 #Increment loop

print(f"30000000th Number: {numbers[-1]}")
