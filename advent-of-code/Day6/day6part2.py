with  open("day6formsanswers.txt", "r") as file:
    readFile = file.read().split('\n') #Split file into array of segments divided line breaks

answers_matrix = [] #Matrix stores each array of answers
answer_count = 0 #Answer count variable stores number of unique answers

answers = [] #Temporary answer array changes with each iteration

for line in readFile:

    if line == '': #If the line is empty (linebreak), append finished answer the filled answer matrix
        answers_matrix.append(answers)
        answers = []

    else: #Otherwise, continue to add to the answer array
        answers.append(line.split('\n')[0])

#Iterate through answers and evaluate
for answer_set in answers_matrix:

    #Iterate through segments of answer (sub-answers for each user)
    for char in answer_set[0]:
        everyoneAnswered = True #For every character, keep track of whether everyone has answered this character or not

        for segment in answer_set:
            if not char in segment: #If this character is not in one of the answer sequences, everyone did NOT answer
                everyoneAnswered = False
                break

        if everyoneAnswered: #If this answer is in everyone's answers, increment answer count
            answer_count += 1

print(f"Answer Count: {answer_count}") #Output result
