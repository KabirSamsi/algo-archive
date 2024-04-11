# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
       
    def add_end(self, val):
        head = self
        while head.next != None:
            head = head.next           
        head.next = ListNode(val)

    def print(self):
        head = self
        while head != None:
            print(head.val)
            head = head.next

class Solution(object):
    def swapPairs(self, head):
        if head == None: #Base Case – list is empty
            return None

        tracker = head #Temporary iterator tracker
        while tracker.next != None: #While list has elements
            nextval = tracker.next #Track next element

            #Now recursively swap remaining elements.
            #Let tracker's next value become the remaining swapped list
            tracker.next = self.swapPairs(nextval.next)

            #Modify so that nextval comes before tracker
            nextval.next = tracker
            return nextval #Return nextval as new head

head = ListNode(1)
head.add_end(2)
head.add_end(3)
head.add_end(4)
head.print()

print("SOLVING")

sol = Solution()
head = sol.swapPairs(head)

print("SOLUTION")
head.print()