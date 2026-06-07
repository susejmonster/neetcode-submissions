# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        part_1 = ListNode(0)
        part_2 = ListNode(0)
        p1tail = part_1
        p2tail = part_2
        
        cur = head
        while cur!=None:
            if cur.val < x:
                p1tail.next = cur
                p1tail = p1tail.next
            else:
                p2tail.next = cur
                p2tail = p2tail.next
            cur = cur.next
        
        p2tail.next = None
        p1tail.next = part_2.next

        return part_1.next