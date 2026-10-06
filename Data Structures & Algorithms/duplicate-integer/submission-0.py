class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        snums = set()
        for each in nums:
            if each in snums:
                return True
            else:
                snums.add(each)
        return False
