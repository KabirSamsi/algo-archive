#Recursive function adds valid bags until it is no longer incrementing new bags
def count_bags(bagset, luggage, prev_count):

    #Bagset stores the incrementing set of bags; Luggage stores the constant array of all bags
    #Previous Count is what creates the stop condition. Stores the length of the bagset from the previous iteration (so program can check whether the bagset is still being incremented)

    for bag in bagset: #Iterate through the incrementing set of bags
        for group in luggage: #Go through each bag set in luggage

            for b in group.contents: #All of the bags that the bag can hold

                if b.val == bag.val and group not in bagset: #If the current bag (from the incrementing bag set) is in this bag group, then the group is valid. Add it to the bagset
                    bagset.append(group)

    if len(bagset) == prev_count: #If the result of this iteration is the same as the last one (bags are no longer being incremented)
        return len(bagset) - 1 #Subtract the start bag from the list (bag cannot store itself)

    else: #If list is still being incremented, repeat function
        return count_bags(bagset, luggage, len(bagset))
