# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        # Step 1: Create a dummy node to handle edge cases (like left = 1)
        dummy = ListNode(0)
        dummy.next = head
        
        # Step 2: Reach the node just before the 'left' position
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
            
        # Step 3: Start reversing the sublist
        # 'curr' is the first node to be reversed
        curr = prev.next 
        
        # We need to do (right - left) swaps
        for _ in range(right - left):
            # 'temp' is the node we want to pull to the front of the sublist
            temp = curr.next
            
            # Rearrange the pointers to move 'temp' behind 'prev'
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
            
        # Step 4: Return the new head
        return dummy.next
