# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        ##down -> ptr to left and right children
        ##up -> sum of included nodes
        def trav(node):
            if node is None:
                return 0
            
            ##in ragne
            if node.val >= low and node.val <= high:
                currsm = node.val##saving a value
            else: 
                currsm = 0
            
            #explore left child right child and return sum of both
            left=trav(node.left)
            right = trav(node.right)
            return left+right + currsm
        
        return trav(root)
        