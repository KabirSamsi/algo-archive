def convert_to_bytes(num, bitmask): #Convert from decimal to binary
    result = str(bin(num))[2:] #Binary encoding of number, as a string
    remainder = "" #Holds the remaining digits
    final = "" #Value after comparing bitmask and encoded binary string

    for x in range(36-len(result)): #Adds '0' for every value not part of the binary sequence
        remainder += '0'

    result = remainder+result #Concatenate remainder string and result string

    for x in range(len(bitmask)): #Compare bitmask to result. If the bitmask value is 'X', add the result value to the final string. Otherwise, the result value is overwritten
        if bitmask[x] != 'X':
            final += bitmask[x]
        else:
            final += result[x]

    return final

def debin(bin_str): #'De-binary' = Convert from binary to decimal
    result = 0 #Final Decimal value
    for x in range(len(bin_str.rstrip('\n'))):
        if int(bin_str[x]) == 1: #If the value in the binary sequence is 1 (meaning it is to be added to the integer value)
            result += 2**(36-(x+1)) #Read binary - add 2^position to the total (algorithm modified because of array indexing)

    return result #Return final result

def convert_to_bytes2(num, bitmask): #Convert from decimal to binary (Version 2)
    result = str(bin(num))[2:] #Binary encoding of number, as a string
    remainder = "" #Holds the remaining digits
    final = "" #Value after comparing bitmask and encoded binary string

    for x in range(36-len(result)): #Adds '0' for every value not part of the binary sequence
        remainder += '0'

    result = remainder+result #Concatenate remainder string and result string

    for x in range(len(bitmask)): #Compare bitmask to result. If the bitmask value is 'X', add the result value to the final string. Otherwise, the result value is overwritten
        if bitmask[x] == '0': #If 0, result is overwritten
            final += result[x]
        else: #If 1, normal value is added. If it is X, it is added, but modified later
            final += bitmask[x]

    return final

def debin2(bin_str): #Convert from binary to decimal but with different string versions (Version 2)
    result_strings = [''] #Starting list of strings
    results = [] #Stores processed binary strings as integers

    if bin_str.count('X') == 0: #If there are no 'X's in the string, just add the one string
        results.append(debin(bin_str))

    else:
        pos = 0 #Position in binary string
        while pos < len(bin_str): #Iterate through binary string
            new_strings = [] #Temporary array of new binary strings, which resets with each iteration

            for result_string in result_strings:
                if bin_str[pos] == 'X': #If the value is X, duplicate the array into one which contains 1 as the new value, and one which contains 0 s the new value
                    new_strings.append(result_string + '0')
                    new_strings.append(result_string + '1')
                else: #If the value is 1 or 0, add the next term
                    new_strings.append(result_string + bin_str[pos])

            result_strings = [] #Clear all previous strings
            for new_string in new_strings: #Add all the new strings
                result_strings.append(new_string)

            pos += 1 #Increment loop

    for r in result_strings: #Convert all binary sequences to numbers using original debin() function
        results.append(debin(r))

    return results
