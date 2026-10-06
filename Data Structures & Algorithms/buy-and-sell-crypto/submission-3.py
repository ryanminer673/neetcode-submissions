class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = 0
        max = 0
        best = 0
        for i, each in enumerate(prices):
            if i == 0:
                min = each
                max = 0
            else:
                if each < min:
                    min = each
                    max = 0
                elif each > max:
                    max = each
            if best < max - min:
                best = max - min
        return best

            