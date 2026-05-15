# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = head
        count = 0 
        while curr:
            count = count + 1
            curr = curr.next
        
        removeidx = count - n
        if removeidx == 0:
            return head.next
        
        idx = 0
        curr2 = head
        while curr2.next and idx < removeidx-1:
            idx = idx + 1
            curr2 = curr2.next
        
        curr2.next  = curr2.next.next
        return head