# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None #stop 
        newHead = head
        if head.next:#stop one element off as we are using two points
            newHead = self.reverseList(head.next) #reverse the edge
            head.next.next = head
        head.next  = None #break the edge
        return newHead
        