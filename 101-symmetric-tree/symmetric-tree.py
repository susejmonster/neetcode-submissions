# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool: 
        ##from root, store left pointer and right pointer
        ##trav both trees with left p go right and right q go left
        ##if p==q True
        ##if p!=q False
        left = root.left
        right = root.right
        def trav(l,r):
            if not l and not r:
                return True
            if not l or not r or r.val!=l.val:
                return False

            right = trav(l.right,r.left)
            left = trav(l.left,r.right)
            return right and left

        return trav(left,right)
        

