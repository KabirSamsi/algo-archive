from day2password2 import Password

with open("day2passwords.txt", 'r') as file:
    valid_passwords = []

    # Iterate through each line in the file and evaluate it
    for line in file:
        elements = line.split(' ') #Break line into elements divided by space; these can be manipulated to represent the letter, occurrence spots, and password

        letter = elements[1].split(':')[0] #Extract letter from file line
        occurrence_spots = (int(elements[0].split('-')[0])-1, int(elements[0].split('-')[1])-1) #Extract the two positions and store them in a tuple (subtract 1 to account for 0-index)
        pwd = elements[2] #Extract password

        password = Password(letter, occurrence_spots, pwd) #Create Password object to store these three characteristics

        #Check for occurrence of letter in the two occurrence spots
        occurrences = 0
        for occurrence_spot in password.occurrence_spots:
            if password.pwd[occurrence_spot] == letter:
                occurrences += 1

        if occurrences == 1: #If exactly one of the two spots has the letter (cannot be 0, cannot be both), then it is valid
            valid_passwords.append(password)

# Output the length of valid passwords
print(f"Valid Passwords: {len(valid_passwords)}")
