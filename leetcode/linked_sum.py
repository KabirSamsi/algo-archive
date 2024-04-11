# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        if l1 == None and l2 == None: #Edge case – two empty lists
            return None
        
        summed_head = ListNode() #Track LL
        summed_iter = summed_head #Iterator LL var
        carry_over = 0 #Stack next decimal place to carry forward
        while l1 != None and l2 != None:
            current = (carry_over + l1.val + l2.val) #Calculate total sum
            #Algorithm explanation – compute remainder from nearest 10 mult.
            #Then divide by ten to carry up in digits.
            carry_over = (current-(current%10))/10 #Update carry
            summed_iter.val = current%10 #Extracts by current pos
            if (l1.next != None or l2.next != None): #If list ended, don't add new
                summed_iter.next = ListNode()
                summed_iter = summed_iter.next
            l1 = l1.next
            l2 = l2.next
        
        if l1 == None: #L1 terminates first
            while l2 != None: #Iterate through remainder of L2
                #Ref. earlier method for next operations
                current = (carry_over + l2.val)
                carry_over = (current-(current%10))/10
                summed_iter.val = current%10
                if (l2.next != None): #Note: Only check for l2
                    summed_iter.next = ListNode()
                    summed_iter = summed_iter.next
                l2 = l2.next

        if l2 == None: #L2 terminates first
            while l1 != None:
                #Ref. earlier method for next operations
                current = (carry_over + l1.val)
                carry_over = (current-(current%10))/10
                summed_iter.val = current%10
                if (l1.next != None): #Note: Only check for l1
                    summed_iter.next = ListNode()
                    summed_iter = summed_iter.next
                l1 = l1.next

        #If carried remainder > 0, add a final slot for the remainder
        if carry_over != 0:
            summed_iter.next = ListNode(carry_over, None) #No next ptr
        
        return summed_head #Returned headptr (NOT tailptr).