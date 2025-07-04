# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prev = None
        curr =head

        while curr:  #when curr is not null
        # 1. store the next node
            next_temp = curr.next
        # 2. flip the pointer
            curr.next = prev
        # 3. move the prev forward
            prev = curr
        # 4. move the curr forward 
            curr = next_temp

        return prev # prev is the new head



        