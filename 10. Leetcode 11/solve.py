class Solution:
    def maxArea(self, height: List[int]) -> int:
        mostArea=0
        l=0
        r=len(height)-1
        while l<r:
            localMax=(r-l)*min(height[r],height[l])
            print(localMax)
            if localMax>mostArea:
                mostArea=localMax
            
            #l+=1
            
            #It works without this with the same complexity
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        
        return mostArea

    
        