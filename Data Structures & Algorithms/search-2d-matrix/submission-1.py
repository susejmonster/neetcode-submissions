class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            l = 0
            r = len(matrix) - 1
            i = 0 

            for i in range(0, len(matrix)):
                while l < r:
                    mid = l + (r-l)//2
                    if matrix[i][mid] < target:
                        l = mid + 1
                    elif matrix[i][mid] > target:
                        r = mid - 1
                    elif matrix[i][mid] == target:
                        return True

            return False