# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        def trav(node,res):
            if node is None:
                return []
            
            
            trav(node.left,res)
            res.append(node.val)
            trav(node.right,res)
            return res
        return trav(root, [])
