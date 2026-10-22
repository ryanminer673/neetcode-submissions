class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # start wuth l and r at 0
        #iterate r until condition not met
        #iterate l until condition remet 
        # save the max of r-l as the max profit

        l = 0
        r = 0
        best = 0

        while r < len(prices):

            while r < len(prices) and prices[r] > prices[l]:
                best = max(best, prices[r] - prices[l])
                r += 1

            if l < r:
                l+=1
            else:
                r+=1
        return best