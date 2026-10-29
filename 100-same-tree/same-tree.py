# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #preorder traversal
        #o(n)
        
        def inorder(node1,node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:
                return False

            if node1.val != node2.val:
                return False
            
            if not inorder(node1.left,node2.left):
                return False
            if not inorder(node1.right ,node2.right):
                return False
            
            return True
        res = inorder(p,q)
        return res

        
