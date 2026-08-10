class Solution:
    def maximumValue(self, n: int, s: int, m: int) -> int:
        if n == 1:
            return s

        numberOfIncreases = n // 2
        numberOfDecreases = numberOfIncreases - 1

        return s + numberOfIncreases * m - numberOfDecreases