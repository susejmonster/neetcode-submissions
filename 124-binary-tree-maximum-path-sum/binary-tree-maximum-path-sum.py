# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        mx = -float('inf')

        def trav(node):
            nonlocal mx
            if node is None:
                return 0
            l = max(0,trav(node.left))
            r = max(0,trav(node.right))

            if mx<node.val + l + r:
                mx = node.val+l+r
            
            return node.val+max(l,r)
        
        trav(root)
        return mx