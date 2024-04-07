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

        if passports[x]["byr"].isdigit() and len(passports[x]["byr"]) == 4 and int(passports[x]["byr"]) in range(1920, 2003): #Validate birth year
            if passports[x]["byr"].isdigit() and len(passports[x]["iyr"]) == 4 and int(passports[x]["iyr"]) in range(2010, 2021): #Validate issue year
                if passports[x]["byr"].isdigit() and len(passports[x]["eyr"]) == 4 and int(passports[x]["eyr"]) in range(2020, 2031): #Validate expiry year

                    if passports[x]["hgt"][0:(len(passports[x]["hgt"]) - 2)].isdigit() and len(passports[x]["hgt"]) >= 3: #Make sure height is a number and at least 3 characters
                        if (((passports[x]["hgt"][(len(passports[x]["hgt"]) - 2):] == "in") and (int(passports[x]["hgt"][0:(len(passports[x]["hgt"]) - 2)]) in range(59, 77))) or ((passports[x]["hgt"][(len(passports[x]["hgt"]) - 2):] == "cm") and (int(passports[x]["hgt"][0:(len(passports[x]["hgt"]) - 2)]) in range(150, 194)))): #Validate height
                            if passports[x]["hcl"][0] == '#' and len(passports[x]["hcl"]) == 7: #Make sure hair color starts with '#' and is right length

                                #Validate hair color
                                for char in passports[x]["hcl"][1:]:
                                    if char in "abcdefghijklmnopqrstuvwxyz1234567890":
                                        valid_hcl = True
                                    else:
                                        valid_hcl = False
                                        break

                                if valid_hcl:
                                    if passports[x]["ecl"] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'): #Validate eye colors
                                        if passports[x]["pid"].isdigit() and len(passports[x]["pid"]) == 9: #Validate passport ID
                                            valid_count += 1 #If conditions are met, add passport

print(f"Number of Valid Passports: {valid_count}") #Output final result
