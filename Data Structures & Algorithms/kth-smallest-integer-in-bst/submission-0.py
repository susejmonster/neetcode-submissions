# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    
        res = []

        def DFS(node):
            if node is None:
                return 
            
            if node.left:
                DFS(node.left)
            res.append(node.val)
            if node.right:
                DFS(node.right)

        DFS(root)
        res.sort()
        return res[k-1]
        