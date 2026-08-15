# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        

        prev,curr,n = None,slow.next,None
        slow.next=None
        while curr:
            n = curr.next
            curr.next = prev
            prev=curr
            curr=n

        h1 = head
        h2 = prev

        while h2:
            tmp1,tmp2 = h1.next,h2.next
            h1.next,h2.next = h2,tmp1
            h1,h2 = tmp1,tmp2
        


            