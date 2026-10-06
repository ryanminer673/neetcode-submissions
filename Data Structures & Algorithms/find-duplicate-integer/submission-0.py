class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        set_nums = set()

        for num in nums:
            if num in set_nums:
                return num

            set_nums.add(num)