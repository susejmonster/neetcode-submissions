# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        
        def Inorder(node,res):
            if not node:
                return 0
            right = Inorder(node.right , res)
            left = Inorder(node.left , res)
            res[0] = max(res[0], left + right)
            return max(left, right) + 1
        
        res = [0]
        
        Inorder(root,res)
        return res[0]

        