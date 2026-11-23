class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
       #if diff array of lines are same then they are on same line
       #if dx,dy and theta is same for two pairs,then they are one same line
        cnt=1
        
        for i in range(0,len(points)):
            x = points[i][0]
            y = points[i][1]
            slopes = {}##must be made everytime because:parallel lines, once made everytime for each starting point it resets to 0
            for j in range(i+1,len(points)):
                x2 = points[j][0]
                y2 = points[j][1] 
                
                if x2-x == 0:
                    thet = float(inf)
                else:
                    thet = (y2 - y)/(x2-x)
                
                
                slopes[thet] = slopes.get(thet, 0) + 1##increment cnt in dict
                cnt = max(slopes[thet]+1 , cnt)##since it asks number of points, not number of lines        
        return cnt