# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bfs(self,root,arr):
        q = deque()
        if root:
            q.append(root)
        level = 0 
        while q:
            for i in range(len(q)):
                node = q.popleft()
                arr.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                else:
                    arr.append(None)       
                level+=1
        return arr

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ###do bfs
        ###fill array with bfs for both
        ###if arrays are same, true else false
        tree1=[]
        tree2=[]
        tree1 = self.bfs(p,tree1)
        tree2 = self.bfs(q,tree2)
        if len(tree1) != len(tree2):
            return False
    
        for i in range(0,len(tree1)):
            if tree1[i] != tree2[i]:
                return False
        return True
    

