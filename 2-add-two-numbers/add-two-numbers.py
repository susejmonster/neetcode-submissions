# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        cur = dummy
        curr1 = l1
        curr2 = l2
        while curr1 or curr2 or carry:
            v1 = curr1.val if curr1 else 0
            v2 = curr2.val if curr2 else 0

            curr_sum = v1  + v2 + carry
            carry = curr_sum // 10
            curr_sum = curr_sum%10
            cur.next = ListNode(curr_sum)

            cur = cur.next
            if curr1:
                curr1 = curr1.next
            else:
                None
            if curr2:
                curr2 = curr2.next
            else:
                None

        return dummy.next