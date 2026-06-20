# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        
        curr2 = head
        curr1 = dummy

        while curr1 and curr1.next:
            sum = 0
            curr2 = curr1.next
            deleted = False
            while curr2:
                sum += curr2.val
                if sum == 0:
                    curr1.next = curr2.next
                    deleted = True
                    break
                curr2 = curr2.next
            if not deleted:
                curr1 = curr1.next
            
        return dummy.next
        