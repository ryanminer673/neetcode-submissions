class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            if i == 0:
                stack.append((temp, i))
            
            while stack and temp > stack[-1][0]:
                j = i - stack[-1][1]
                result[stack[-1][1]] = j
                stack.pop()
            stack.append((temp, i))

        return result
        
            