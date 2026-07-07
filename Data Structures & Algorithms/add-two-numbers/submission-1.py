# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        s = self._getNumber(l1) + self._getNumber(l2)
        print(s)
        dummy = ListNode(0)
        cur = dummy
        s = str(s)[::-1]
        for c in s:
            node = ListNode(int(c))
            cur.next = node
            cur = cur.next
        return dummy.next
        
    
    def _getNumber(self, l: Optional[ListNode]):
        temp_str = ''
        while l:
            temp_str = str(l.val) + temp_str
            l = l.next
        return int(temp_str)

        