# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        count = 0
        while curr!=None:
            count+=1
            curr = curr.next
        mid = 0
        if count%2==0:
            mid = count//2
        if count%2!= 0:
            mid = count//2
        
        
        n = 1
        while n <= mid and head!=None:
            head=head.next
            n+=1
        return head