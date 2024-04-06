with open("day6formsanswers.txt", "r") as file:
    readFile = file.read().split('\n') #Split file into array of segments divided line breaks

answers = [] #Array stores each string of answers
ans_count = 0 #Variable stores number of unique answers

answer_string = "" #Temporary answer variable changes with each iteration

for line in readFile:
    if line == '': #If the line is empty (linebreak), append finished answer the accumulated answer string
        answers.append(answer_string)
        answer_string = ""
    else: #Otherwise, continue to accumulate the answer string
        answer_string += line.split('\n')[0]

#Iterate through answers and evaluate
for answer in answers:

    #Iterate through characters of answer
    for x in range(len(answer)):
        if answer.index(answer[x]) == x: #If indices do not match (if the same letter exists earlier in the string), then it will not add to answer_count. If indices match (this is the first instance of a letter), then it is added
            ans_count += 1

print(f"Answer Count: {ans_count}") #Output result
