with open("day4passports.txt", "r") as file:
    passports = [] #Array of passports
    valid_count = 0 #Count of valid passports

    readFile = file.read().split('\n') #Split file into array of segments divided line breaks

    passport = {} #Temporary passport dictionary can be repeatedly changed and added

    for line in readFile:

        if line == '': #If the line is empty (linebreak), append the accumulated passport dict
            passports.append(passport)
            passport = {}

        else: #Otherwise, continue to accumulate the dictionary
            for seg in line.split(): #
                passport[seg.split(':')[0]] = seg.split(':')[1]

#Iterate through passports and check if a) passport has all 8 fields, or b) passport has 7 fields, but is only missing "Country ID"
for x in range(len(passports)):
    if (len(passports[x])) == 8 or (len(passports[x]) == 7 and not ("cid" in passports[x])):
        valid_count += 1 #If conditions are met, add passport

print(f"Number of Valid Passports: {valid_count}") #Output final result
