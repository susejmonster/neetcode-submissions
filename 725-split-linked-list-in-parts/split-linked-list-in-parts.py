# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        curr = head
        length = 0
        #find len of list
        while curr:
            length+=1
            curr=curr.next
        #init res with ele same as number of groups
        n,r = length//k,length%k
        res = [None]*k
        curr=head
        prev = None
        #while cur and size is 1 or less than 1 of valid size, append to cur
        for i in range(k):
            res[i] = curr
            for j in range(n+(1 if r>0 else 0)):
                prev = curr
                curr=curr.next
            if prev:
                prev.next = None
            if r>0:
                r-=1
        
        return res
            

        