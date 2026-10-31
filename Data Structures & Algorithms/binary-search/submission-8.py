class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #binary search 
        # s = 0 e = len(nums)-1
        # middle = e-s//2
        # check middle
        # 

        s = 0
        e = len(nums) - 1
        
        while s <= e:
            middle = s + ((e-s) // 2)

            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                e = middle - 1
            else:
                s = middle + 1

        return -1 
