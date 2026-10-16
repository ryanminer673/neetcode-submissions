class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        s = 0
        e = len(heights) - 1

        max_water = 0

        while s < e:

            
            max_water = max(max_water, (min(heights[s], heights[e]) * (e-s)))


            if heights[s] > heights[e]:
                e -= 1
            else:
                s += 1 

        return max_water 