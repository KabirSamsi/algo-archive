from get_average_length import get_average_length

with open("day16tickets.txt", 'r') as file:
    adding_rules = True #Tracks whether the current activity is adding rules (the first few lines all state rules, so this starts off as true)
    evaluating_my_ticket = False #Tracks whether the current activity is evaluating MY ticket
    evaluating_tickets = False #Tracks whether the current activity is evaluating tickets
    rules = {} #Dictionary stores all the rules as sets
    my_ticket = [] #Array stores information on my ticket
    other_tickets = [] #Matrix stores information on other tickets

    for line in file:
        if adding_rules:
            if line.rstrip('\n') == '': #This stops when the file reaches an empty line, then moves on to some other commands
                adding_rules = False
            else: #Perform string operations on the stated rules and store them as sets in a dictionary of rules
                rule = set()
                for segment in line.rstrip('\n').split(': ')[1].split('or'):
                    for x in range(int(segment.split('-')[0]), (int(segment.split('-')[1]))+1):
                        rule.add(x)
                rules[line.rstrip('\n').split(':')[0]] = rule #Insert this set of allowed positions at the given name value

        if evaluating_my_ticket:
            if line.rstrip('\n') == '': #This stops when the file reaches an empty line, then moves on to some other commands
                evaluating_my_ticket = False

            else: #Perform string operations on the stated rules and store them as range tuples in a matrix of ruls
                ticket_position_strings = line.rstrip('\n').split(',') #Add each number in that ticket to the ticket Ids
                for ticket in ticket_position_strings:
                    my_ticket.append(int(ticket))

        if line.rstrip('\n') == "your ticket:": #This line is when my ticket evaluation starts
            evaluating_my_ticket = True

        if evaluating_tickets: #Execute if file is currently at the 'evaluating ticket' part
            valid = True #Tracks whether ticket is valid
            valid_nums = set()

            #Valid Nums stores ALL allowed numbers
            for ruleset in rules:
                for num in rules[ruleset]:
                    valid_nums.add(num)

            #Store the ticket's positions as numbers
            ticket_position_strings = line.rstrip('\n').split(',')
            ticket_positions = []

            for pos in ticket_position_strings:
                ticket_positions.append(int(pos))

            #Evaluate to see whether ticket is valid or not; if valid, add it to the matrix of other tickets
            for position in ticket_positions:
                if position not in valid_nums:
                    valid = False
                    break
            if valid:
                other_tickets.append(ticket_positions)

        if line.rstrip('\n') == "nearby tickets:": #Signal to start the 'evaluating ticket' part in the file
            evaluating_tickets = True

    other_tickets.append(my_ticket) #Reduce need to evaluate both my ticket and the other tickets
    my_ticket_dictionary = {} #Stores each ticket position, and where it appears in my ticket

    for ruleset in rules: #Set a position for each ruleset in the ticket dictionary to equal an empty array (will fill out in following commands)
        my_ticket_dictionary[ruleset] = []

    counter = 0 #Keeps track of index in each array
    while counter < len(my_ticket):
        valid_position = True #Assume positions are valid when starting off

        for ruleset in rules: #Iterate through each rule key in rules
            for ticket in other_tickets: #Iterate through all tickets
                if ticket[counter] not in rules[ruleset]: #If not in ruleset, it is invalid. Immediately  break loop
                    valid_position = False
                    break
                else: #If it is in this ruleset
                    valid_position = True
            if valid_position == True: #If this is a valid position, add it to the ticket dictionary at its corresponding position
                my_ticket_dictionary[ruleset].append(my_ticket[counter])

        counter += 1 #Increment Counter

    while get_average_length(my_ticket_dictionary) > 1: #Function to get Average Length of Dictionary's arrays
        for d in my_ticket_dictionary:
            if len(my_ticket_dictionary[d]) == 1: #For all the arrays in the dictionary where there is only 1 item (meaning that the correct value HAS to be that one)

                for dic in my_ticket_dictionary: #Iterate through remaining dictionaries and if they contain this value (and are larger than 1), remove it
                    if my_ticket_dictionary[d][0] in my_ticket_dictionary[dic] and len(my_ticket_dictionary[dic]) > 1:
                        my_ticket_dictionary[dic].remove(my_ticket_dictionary[d][0])

    #Multiply values starting with "departure" together to get final result
    departure_product = 1
    for ticket in my_ticket_dictionary:
        if ticket[:9] == 'departure':
            departure_product *= my_ticket_dictionary[ticket][0]

    print(f"Product of departure fields: {departure_product}") #Output result
