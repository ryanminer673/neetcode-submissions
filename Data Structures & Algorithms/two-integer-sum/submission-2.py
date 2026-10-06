class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dnums = dict()

        for i, num in enumerate(nums):
            if target - num in dnums:
                return [dnums[target-num], i]
            dnums[num] = i
        
        return [0, 1]
        