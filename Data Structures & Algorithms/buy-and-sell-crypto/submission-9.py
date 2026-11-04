class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #sliding window
        # keep the start < end
        # at each one save the max 
        # if start >= end, move start until its less that
        
        left = 0
        best = 0

        for right in range(len(prices)):

            while left < right and prices[left] >= prices[right]:
                left += 1

            best = max(best, prices[right] - prices[left])

        return best
