class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        sorted_nums = sorted(nums) #sort list O(nlogn)

        print(sorted_nums)

        result = set()

        # for each number
        for i, num in enumerate(sorted_nums):

            s = 0
            e = len(sorted_nums) - 1

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

                if sorted_nums[s] + sorted_nums[e] == target:
                    valid = [num, sorted_nums[s], sorted_nums[e]]
                    valid.sort()
                    result.add(tuple(valid))
                    s+= 1
                elif sorted_nums[s] + sorted_nums[e] < target:
                    s += 1
                elif sorted_nums[s] + sorted_nums[e] > target:
                    e -= 1
            
        return list(result)
