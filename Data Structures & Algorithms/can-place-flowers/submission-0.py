class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if flowerbed[0]:
            empty = 0
        else:
            empty = 1

        for f in range(0,len(flowerbed)):
            if flowerbed[f]:
               n -= int((empty-1)/2) 
               empty = 0
            else:
                empty += 1
        
        n-=empty//2
        return n<=0