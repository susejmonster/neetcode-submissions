class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        #10,2,5,3-> store half in dict
        #[5,1,2.5,1.5] -> check for each i if i is in dict yet

        for i in range(0,len(arr)):
            for j in range(i+1, len(arr)):
                if arr[j]/2 == arr[i] or arr[i]/2 == arr[j]:
                    return True
        return False