from day2password1 import Password

with open("day2passwords.txt", 'r') as file:
    valid_passwords = []

    # Iterate through each line in the file and evaluate it
    for line in file:
        elements = line.split(' ') #Break line into elements divided by space; these can be manipulated to represent the letter, range of occurrences, and password

        letter = elements[1].split(':')[0] #Extract letter from file line
        occurrence_range = range(int(elements[0].split('-')[0]), int(elements[0].split('-')[1])+1) #Extract allowed occurrence range from file line (range does not include the top value, so add 1)
        pwd = elements[2] #Extract password

        password = Password(letter, occurrence_range, pwd) #Create Password object to store these three characteristics

        if (password.pwd.count(password.letter) in password.occurrence_range): #Evaluate to see if password fits requirements (if the number of letter occurrences is in the required range)
            valid_passwords.append(password)

# Output the length of valid passwords
print(f"Valid Passwords: {len(valid_passwords)}")
