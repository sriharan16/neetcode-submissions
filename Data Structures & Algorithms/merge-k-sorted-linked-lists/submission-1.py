import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        minheap = []
        
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(minheap, (l.val, i, l))
        
        dummy = ListNode()
        tail = dummy

        while minheap:
            _, i, curr = heapq.heappop(minheap)

            tail.next = curr
            tail = tail.next

            if curr.next:
                heapq.heappush(minheap, (curr.next.val, i, curr.next))
        return dummy.next

        



