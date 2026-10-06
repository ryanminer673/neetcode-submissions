class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        Snums = set()
        for num in nums:
            if num in Snums:
                return True
            Snums.add(num)
        return False


