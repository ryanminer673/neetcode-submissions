class Solution:
    def findMin(self, nums: List[int]) -> int:
        #find where the switch is
        # binary search but so that it continues until you find where nums[i] < nums[i-=]
        # you can determing where to search by checking 

        l = 0
        r = len(nums) - 1

        while l < r:
            middle = l + (r-l) // 2

            if nums[middle] > nums[r]:
                # minimum is to the right
                l = middle + 1
            else:
                # middle could be the minimum
                r = middle

        return nums[l]



