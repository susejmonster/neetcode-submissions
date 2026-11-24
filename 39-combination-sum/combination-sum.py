class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ##take candidates one by one in different orders
        ##if the sum ecomes target, add to res
        res = []
        path = []
        def back(i,target):
            #base cases
            #success cases
            if target == 0:
                res.append(path.copy())
                return
            #outofbounds cases
            if i > len(candidates)-1 or target < 0:
                return
            
            
            path.append(candidates[i])
            #include stay at i since duplicates are allowed.
            back(i,  target - candidates[i])
            print(path)
            path.pop()
            #exclude
            back(i+1 , target)
            
      
            
            
        back(0, target)
        return res



            
        