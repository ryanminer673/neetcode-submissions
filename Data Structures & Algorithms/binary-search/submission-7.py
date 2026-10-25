class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low = 0
        high = len(nums)-1

        while low <= high:
            
            middle = low + ((high - low) // 2)

            value = nums[middle]

            if value == target:
                return middle
            
            elif value > target:
                high = middle - 1
            elif value < target:
                low = middle + 1
        return -1
        



        

