# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self,node,s,n):
        if not node:
            return s, n
        
        # Accumulate the current node's value and increment node count
        s += node.val
        n += 1
        
        # Recurse down left and right children, carrying the updated sum and count
        left_s, left_n = self.height(node.left, s, n)
        right_s, right_n = self.height(node.right, s, n)
        
        # Total sum/count for this node's subtree = left result + right result - initial (s, n) offset
        # (Subtracting (s - node.val) and (n - 1) avoids double-counting shared ancestors)
        return (left_s + right_s - (s - node.val)), (left_n + right_n - (n - 1))

    def averageOfSubtree(self, root: TreeNode) -> int:
        cnt = 0
        def traverse(i):
            nonlocal cnt
            if not i:
                return
            
            s,n=self.height(i,0,0)
            avg = s//n
            if avg == i.val:
                cnt+=1
            traverse(i.left)
            traverse(i.right)
        traverse(root)
        return cnt