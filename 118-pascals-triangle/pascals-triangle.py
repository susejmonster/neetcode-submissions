class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        COLS = []
        for j in range(0,numRows):
            row = [1]*(j+1)#each iteration of j is a row, each of i is ele in that row
            for i in range(1,j):#values to fill, avoid if statements for indexing
                    row[i] = COLS[j-1][i-1]+COLS[j-1][i]
            COLS.append(row)
        
        return COLS


