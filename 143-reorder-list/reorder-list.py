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
        if not head:
            return
        nodes = [] 
        curr=head
        while curr!=None:
            nodes.append(curr)
            curr = curr.next
        
        p = 0
        q = len(nodes)-1
        while p<q:
            nodes[p].next = nodes[q]
            p+=1
            if p>=q:
                break
            nodes[q].next = nodes[p]
            q-=1
        nodes[p].next = None
            