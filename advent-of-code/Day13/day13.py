with open("day13buses.txt", 'r') as file:
    data = [] #Data from file
    for line in file:
        data.append(line)

    buses = [] #Array keeps track of each bus

    for segment in data[1].split(','): #Add buses listed in second line of file to array
        if segment != 'x':
            buses.append(int(segment))

    timestamp = int(data[0]) #Current starting point, as given in file
    earliest_found = False #Tracks whether the earliest timestamp has been accessed yet
    product = 1

    while not earliest_found: #Continue loop until earliest value is found
        for bus in buses:
            if timestamp%bus == 0: #When the first timestamp divisible by bus ID is found, get product and break loop
                product = (timestamp-int(data[0])) * bus #Product equals the difference between the timestmap and starting timestamp, multiplied by the bus ID
                earliest_found = True
                break
        timestamp += 1 #Otherwise, continue to increment time

    print(f"Product: {product}") #Output result
