class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        result = set()

        # for each number
        for i, num in enumerate(nums):

            s = 0
            e = len(nums) - 1

            target = 0 - num

            # 2 pounter approach converging
            while s < e:
                
                # account for reusing values
                if s == i:
                    s += 1
                    continue
                if e == i:
                    e -= 1
                    continue

                if nums[s] + nums[e] == target:
                    valid = [num, nums[s], nums[e]]
                    valid.sort()
                    result.add(tuple(valid))
                    s+= 1
                elif nums[s] + nums[e] < target:
                    s += 1
                elif nums[s] + nums[e] > target:
                    e -= 1
            
        return list(result)
