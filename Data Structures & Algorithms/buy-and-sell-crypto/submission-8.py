class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #find the largets diffrent between 2 numbers sequential

        #valid window - left is <= right
        # invalid window left > right

        #
        # move right
        # check if price at left > prices at right
        # until left is greater than right 
        # if left is grater than right move left until its not
        

        l = 0
        best = 0

        for r in range(len(prices)):

            while prices[l] > prices[r]:
                l+=1

            best = max(best, prices[r] - prices[l])

        return best

