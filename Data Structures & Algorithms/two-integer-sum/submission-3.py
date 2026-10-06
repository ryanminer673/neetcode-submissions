class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Seen = {} 

        for i, num in enumerate(nums): #O(n)
            if target - num in Seen: #O(1)
                return [Seen[target-num], i] 
            Seen[num] = i #O(1)


        