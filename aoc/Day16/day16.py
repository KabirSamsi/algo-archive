with open("day16tickets.txt", 'r') as file:
    adding_rules = True #Tracks whether the current activity is adding rules (the first few lines all state rules, so this starts off as true)
    evaluating_tickets = False #Tracks whether the current activity is evaluating tickets
    rules = []
    invalid_count = 0

    for line in file:
        if adding_rules:
            if line.rstrip('\n') == '': #This stops when the file reaches an empty line, then moves on to some other commands
                adding_rules = False
            else: #Perform string operations on the stated rules and store them as range tuples in a matrix of ruls
                for segment in line.rstrip('\n').split(': ')[1].split('or'):
                    rules.append((int(segment.split('-')[0]), (int(segment.split('-')[1]))+1)) #Add 1 because range excludes the last number

        if evaluating_tickets:
            ticket_position_strings = line.rstrip('\n').split(',') #Add each number in that ticket to the ticket Ids
            ticket_positions = []
            for ticket in ticket_position_strings:
                ticket_positions.append(int(ticket))

            for ticket in ticket_positions: #Evaluate to see whether each number is in the listed ranges or not. If it is not, then it is invalid
                valid = False
                for ruleset in rules:
                    if ticket in range(ruleset[0], ruleset[1]):
                        valid = True
                        break
                if not valid:
                    invalid_count += ticket

        if line.rstrip('\n') == "nearby tickets:": #This line is when the ticket evaluation starts
            evaluating_tickets = True

    print(f"Error Rate: {invalid_count}") #Output result
