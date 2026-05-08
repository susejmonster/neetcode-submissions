# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
          dummy = ListNode()
          last = dummy

          while list1 and list2:
               
               if(list1.val <= list2.val):
                   last.next = list1
                   list1 = list1.next
               elif(list1.val > list2.val):
                   last.next = list2
                   list2 = list2.next
               
               last = last.next
          last.next = list1 if list1 else list2
          return dummy.next