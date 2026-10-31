class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        s = 0
        e = len(numbers) - 1

        while s < e:
            total = numbers[s] + numbers[e]
            if total == target:
                return [s+1, e+1]

            if total > target:
                e -= 1
            
            else:
                s += 1
        
        return []