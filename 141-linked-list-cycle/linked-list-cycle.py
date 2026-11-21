# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ##no head return -1
        if not head:
            return False
        ##make hashtable of length list
        hash = {}
        ##fill value in each postion
        curr = head
        while curr:
            ##if value already exist, cycle true, else false
            if curr in hash:
                return True
            hash[curr] = True
            curr=curr.next
        return False