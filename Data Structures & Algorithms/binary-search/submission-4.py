class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        while low <= high:
            pivot = low + math.ceil((high-low) / 2)
            if nums[pivot] == target:
                return pivot
            elif nums[pivot] < target:
                low = pivot + 1
            elif nums[pivot] > target:
                high = pivot - 1
        
        return -1



        

