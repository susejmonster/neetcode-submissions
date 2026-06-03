# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        nodes = [] 
        curr = head
        while curr!=None:
            nodes.append(curr)
            curr=curr.next
            
        l = len(nodes)
        rem = l - n
        if rem == 0:
            return head.next
        
        nodes[rem-1].next = nodes[rem].next
        return head