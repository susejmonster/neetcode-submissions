# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = list1
        curr_1 = list2
        arr = []
        while curr!=None:
            arr.append(curr.val)
            curr = curr.next
        while curr_1!=None:
            arr.append(curr_1.val)
            curr_1 = curr_1.next
        if not arr:
            return None

        arr.sort()

        head = ListNode(arr[0])
        curr_2 = head
        for n in range(1,len(arr)):
            tmp =  ListNode(arr[n])
            curr_2.next = tmp
            curr_2 = curr_2.next
        return head