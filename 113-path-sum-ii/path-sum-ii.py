# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        path = []

        def dfs(node,cursum):
            if node is None:
                return 
            
            cursum+=node.val
            path.append(node.val)
            if node.right == None and node.left == None and cursum == targetSum:
                paths.append(path[:])
            dfs(node.left,cursum)
            dfs(node.right,cursum)
            path.pop()

        dfs(root,0)
        return paths