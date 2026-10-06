class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        snums = set() #O(n) space complexity

        for num in nums: #O(n) worst case time complexity
            if num in snums:
                return True
            snums.add(num)

        return False
       

