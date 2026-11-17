class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # this will be a 2 pointer solution
        # ill have to converge pointers on some condition
        # stor the best 

        r = len(heights)-1
        l = 0

        best = 0

        while l < r:

            best = max(best, (r-l) * min(heights[l], heights[r]))
            
            # converge on whichever next value is larger
            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1

        return best

            