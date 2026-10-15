class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        result = [1]* len(nums)

        s = 0
        e = len(nums) - 1

        while s <= len(nums) -1 and e >= 0:
            if s == 0:
                prefix[s] = nums[s]
            else:
                prefix[s] = prefix[s-1] * nums[s]


            if e == len(nums) - 1:
                suffix[e] = nums[e]
            else:
                suffix[e] = suffix[e+1] * nums[e]

            s += 1
            e -= 1

        for i in range(len(nums)):
            if i == 0:
                result[i] = suffix[i+1]
            elif i == len(nums) - 1:
                result[i] = prefix[i-1]
            else:
                result[i] = prefix[i-1] * suffix[i+1]

        return result