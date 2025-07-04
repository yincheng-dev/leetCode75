# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        current = dummy

        while l1 and l2:
            if l1.val > l2.val:
                current.next = l2
                l2 = l2.next
            else: 
                current.next = l1
                l1 = l1.next
            # Move the current pointer forward one step in the newly built merged list 
            current = current.next
        # Attch the remining nodes
        # if l1 is not none, else l2 ,if l2 is not non 
        current.next = l1 if l1 else l2    
        return dummy.next




        