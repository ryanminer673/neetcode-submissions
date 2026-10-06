class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        snums = set()
        for num in nums:
            if num in snums:
                return True
            snums.add(num)
        return False
