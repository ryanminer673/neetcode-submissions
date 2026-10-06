class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dnums = dict()
        for i, each in enumerate(nums):
            if ((target - each) in dnums):
                return [dnums[target-each], i]
            else:
                dnums[each] = i
        return False
        