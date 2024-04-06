#3-Ary Tree holds each node with a value that connects to three other nodes - First, Second and Third
class Node:

    def __init__(self, val, seq, parent):
        self.val = val #Value
        self.parent = parent #The node which this node stems from (start node has a null value here)
        self.sequence_count = 0 #Number of full sequences that stem from this node

    #Process the first child node (1 + the value)
        if self.val+1 == seq[len(seq)-1]: #If the sequence succesfully reaches the end of the array, 'stop' signal stops building this branch (Works like DNA Stop Codon)
            self.first = "stop"
            self.increment_sequence_count() #Since the sequence is successful, call the increment_sequence_count() method
        elif (self.val)+1 in seq: #If there is a point in the array that is 1+value and the end has not been reached
            self.first = Node(self.val+1, seq, self) #Recursively create another node, and so on and so forth, until this branch cannot be extended any longer
        else: #If 1+value is not in the array
            self.first = None

    #Process the second child node (2 + the value)
        if self.val+2 == seq[len(seq)-1]: #If the sequence succesfully reaches the end of the array, 'stop' signal stops building this branch
            self.second = "stop"
            self.increment_sequence_count() #Since the sequence is successful, call the increment_sequence_count() method
        elif self.val+2 in seq:
            self.second = Node(self.val+2, seq, self) #Recursively create another node, and so on and so forth, until this branch cannot be extended any longer
        else: #If 2+value is not in the array
            self.second = None

    #Process the third child node (3 + the value)
        if self.val+3 == seq[len(seq)-1]: #If the sequence succesfully reaches the end of the array, 'stop' signal stops building this branch
            self.third = "stop"
            self.increment_sequence_count() #Since the sequence is successful, call the increment_sequence_count() method
        elif self.val+3 in seq:
            self.third = Node(self.val+3, seq, self) #Recursively create another node, and so on and so forth, until this branch cannot be extended any longer
        else: #If 3+value is not in the array
            self.third = None

    def increment_sequence_count(self): #Every time a node successfuly completes a sequence (hits the final value in the array, the adaptor rating) then increment the sequence and recursively add it to each higher parent (at the end, the original node will have the full count)
        self.sequence_count += 1
        if self.parent != None:
            self.parent.increment_sequence_count() #Recursively performs this function until there is no parent
