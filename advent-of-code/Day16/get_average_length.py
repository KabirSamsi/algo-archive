#Function to get the average length of all arrays in the dictionary
def get_average_length(dictionary):
    length = 0

    for arr in dictionary: #Iterate through each array stored in the dictionary, and sum up its length
        length += len(dictionary[arr])

    length /= len(dictionary) #To take average, divide by number of arrays

    return length
