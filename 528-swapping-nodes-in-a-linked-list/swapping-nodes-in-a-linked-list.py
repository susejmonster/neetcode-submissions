# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = head
        n = 0
        while count!=None:
            n+=1
            count = count.next

        K = 0
        curr1 = head
        curr2 = head
        while curr1 and K<k-1:
            K +=1
            curr1 = curr1.next
        K = 0
        while curr2 and K<(n-k):
            K+=1
            curr2 = curr2.next
        
        curr1.val,curr2.val = curr2.val,curr1.val
        return head