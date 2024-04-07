from day7bagset import BagSet
from day7countbags import count_bags

with open("day7luggage.txt", 'r') as file:
    readFile = [] #Array stores file separated by linebreaks
    luggage = [] #Array stores all bagsets

    for line in file:
        readFile.append(line.strip('.\n'))

for line in readFile:
    bagset = BagSet(line.split('contain')[0].strip(), []) #Creates BagSet object (See day7bagset.py)
    luggage.append(bagset) #add to luggage

for line in readFile:

    for b in luggage:
        if b.val == line.split('contain')[0].strip():
            bagset = b

    if not line.split('contain')[1].strip() == "no other bags": #If there ARE some bags the bag can hold

        #Search for BagSet objects whose value includes the string (using 'in' instead of == because of singular/plural)
        for bag in line.split('contain')[1].strip().split(', '):
            for b in luggage:
                if bag[2:] in b.val:
                    bagset.contents.append(b)

#Search for the start bag (in my input file, "Shiny Gold Bag") and set it as the starting bag in the recursive count_bags() function
for bagset in luggage:
    if bagset.val == "shiny gold bags":
        start_bag = bagset
        break

print(f"Number of bags that can hold my bag: {count_bags([start_bag], luggage, 0)}") #Print output by performing recursive function (see day7countbags.py)
