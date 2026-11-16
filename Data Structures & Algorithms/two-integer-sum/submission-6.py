class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        # for each number i look up if i have seen the number needed to get the target
        # to get the index i have to store the num as the key for lookup and the idex as the value

        seen = {}
        for i, num in enumerate(nums):
            if target-num in seen:
                return [seen[target-num], i]
            seen[num] = i
        return []
