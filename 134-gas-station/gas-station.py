class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        i = len(gas)-1
        j = 0
        total = gas[i] - cost[i]

        while j<i:
            if total < 0:
                i-=1
                total+=gas[i]-cost[i]
            else:
                total+=gas[j]-cost[j]
                j+=1
        if total>=0:
            return i 
        else:
            return -1