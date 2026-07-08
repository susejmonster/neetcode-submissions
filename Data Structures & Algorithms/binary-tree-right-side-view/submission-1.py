# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        def dp(node,depth):
            if node is None:
                return 

            if depth == len(res):
                res.append(node.val)

            dp(node.right,depth+1)
            dp(node.left,depth+1)

        dp(root,0)
        return res