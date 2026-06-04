# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #go through each node
        #at each node check depth of left subtre and right subtree
        #store res as true, if depth is leftheight - rightheight <= 1,do nothinmg,else break
        if not root:
            return True
        leftHeight = self.maxHeight(root.left)
        rightHeight = self.maxHeight(root.right)
        if abs(leftHeight - rightHeight) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
    def maxHeight(self,root):
        if not root:
            return 0 
            
        return 1+max(self.maxHeight(root.left), self.maxHeight(root.right))
        