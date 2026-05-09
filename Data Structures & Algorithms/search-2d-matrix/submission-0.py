class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            l = 0
            r = len(matrix) - 1
            i = 0 

            for i in range(0, len(matrix)):
                while l < r:
                    mid = l + (r-l)//2
                    if matrix[mid][i] < target:
                        l = mid + 1
                    elif matrix[mid][i] > target:
                        r = mid - 1
                    else:
                        return True

            return False