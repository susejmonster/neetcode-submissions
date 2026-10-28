# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if len(preorder)==0 or len(inorder)==0:
            return None
        mp = {value: index for index, value in enumerate(inorder)}
        def Build(i,j,n):
            if n<=0:
                return None
            #caclulate the left subtree, then the right subtree from this node
            root = preorder[i]
            root_pos  = mp[root]
            left_tree = root_pos - j
            #attach them
            left = Build(i+1 , j , left_tree)
            right = Build(i+1+left_tree , root_pos+1 , n - left_tree - 1)
            return TreeNode(root , left , right)

        return Build(0,0,len(preorder))