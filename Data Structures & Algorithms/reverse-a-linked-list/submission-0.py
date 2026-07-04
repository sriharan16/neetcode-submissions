# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            rhead = head
            head = head.next
            rhead.next = None
            # head = head.next()
        else:
            return None

        while head:
            temp = head
            head = head.next
            
            temp.next = rhead
            rhead = temp
            
        return rhead