class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        best = 0

        while l < r:
            if heights[r] > heights[l]:
                water_held = heights[l] * (r - l)
                l += 1
            else:
                water_held = heights[r] * (r - l)
                r -= 1
            best = max(water_held, best)
        return best
