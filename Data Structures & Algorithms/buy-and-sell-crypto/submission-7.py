class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #sliding window 
        # the window state is valid while prices[end] >= prices[start]
        # its invalid while prices[end] < prices[start]

        left = 0
        best = 0

        for right in range(len(prices)):

            while prices[left] > prices[right]:
                left += 1

            best = max( prices[right] - prices[left], best)

        return best

            
            

        