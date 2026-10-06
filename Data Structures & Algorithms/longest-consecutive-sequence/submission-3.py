
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if nums == []:
            return 0


        snums = set(nums)
        acc = 1
        highest = 1

        for num in nums:
            if num-1 in snums:
                continue
            else:
                while num+1 in snums:
                    acc +=1
                    if highest < acc:
                        highest = acc
                    num = num+1
                acc = 1
        return highest
                

        


