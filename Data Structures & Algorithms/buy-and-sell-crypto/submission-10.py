class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # sliding window
        # i reduce the window by acc left
        # i start acc left if r > left and i stop when 
        # l == r or the val at left is <= value at right

        left = 0

        best = 0

        for right in range(len(prices)):

            while left <= right and prices[left] > prices[right]:
                left += 1

            best = max(best, prices[right] - prices[left])

        return best

            