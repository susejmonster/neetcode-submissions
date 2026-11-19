# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        ##TRAVERSE TILL NODE == VAL
        def find(node,val):
            if not node:
                return None
            
            if node.val == val:
                return node
            left = find(node.left,val)
            right = find(node.right,val)
            return left or right
        found = find(root,val)
        return found
        