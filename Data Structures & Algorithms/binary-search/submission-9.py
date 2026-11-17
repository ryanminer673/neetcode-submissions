class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # get the middle value
        # get the first and last
        # of th emiddle value is > update the last to be the middle 
        

        start = 0
        end = len(nums)-1

        while start <= end:
            middle = start + (end - start) // 2

            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                end = middle-1
            else:
                start = middle + 1

        return -1
