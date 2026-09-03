class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        
        
        #but how to store i,j?
        for i in range(rows):
            for j in range(i+1,cols):
                matrix[j][i],matrix[i][j]=matrix[i][j],matrix[j][i]
        
        for i in range(rows):
            matrix[i].reverse()
                       
        
        return matrix