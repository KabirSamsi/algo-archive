#Recursive function adds necessary bags until it is no longer incrementing new bags
def count_bags(bagset, luggage, prev_total):

    #Bagset stores the incrementing sets of bags in a tree-like structure - each row of the matrix represents a deeper level of
    #Previous Total is what creates the stop condition. Stores the total from the previous iteration (so program can check whether the bagset is still being incremented)

    bagRow = {} #Temporary Bag Row dictionary stores all of the bags and their counts in each level of bags

    for bag in bagset[-1]: #Iterate through the previous row of bagset
        for content in bag.contents: #Each bag contained inside the row

            #If the contained bag is already included in the new bag Row, add to it
            if content in bagRow:
                bagRow[content] += bag.contents[content] * bagset[len(bagset) - 1][bag]

            #Otherwise, initialize it
            else:
                bagRow[content] = bag.contents[content] * bagset[len(bagset) - 1][bag]

    bagset.append(bagRow) #Add the filled dictionary as a row in the bagset matrix

    #Increment total number of bags based on bagset
    total = 0
    for br in bagset:
        for bag in br:
            total += br[bag]

    if total == prev_total: #If the result of this iteration is the same as the last one (bags are no longer being incremented)
        return total -1 #Subtract the start bag from the list (bag cannot store itself)

    else: #If list is still being incremented, repeat function
        return count_bags(bagset, luggage, total)
