# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        tail = head
        while list1 or list2:
            print(head.val, tail.val)
            if not list1:
                tail.next = list2
                break
            elif not list2:
                tail.next = list1
                break
            else:
                if list1.val <= list2.val:
                    tail.next = list1
                    list1 = list1.next
                else: 
                    tail.next = list2
                    list2 = list2.next
                tail = tail.next
            
        return head.next
        