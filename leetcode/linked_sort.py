class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        merged_head = ListNode()
        merged = merged_head
        c1 = list1
        c2 = list2

        if c1 == None:
            return c2
        elif c2 == None:
            return c1

        if c1.val > c2.val:
            merged.val = c1.val
            c1 = c1.next
        else:
            merged.val = c2.val
            c2 = c2.next

        while (c1 != None and c2 != None):
            if c1.val < c2.val:
                merged.next = ListNode(c1.val, None)
                c1 = c1.next
            else:
                merged.next = ListNode(c2.val, None)
                c2 = c2.next
            merged = merged.next
        
        if c1 == None:
            while (c2 != None):
                merged.next = ListNode(c2.val, None)
                c2 = c2.next
                merged = merged.next
        else:
            while (c1 != None):
                merged.next = ListNode(c1.val, None)
                c1 = c1.next
                merged = merged.next
        
        return merged_head
    
