class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        Open = {'(', '[', '{'}
        Close = {')':'(', ']':'[', '}':'{'}

        for char in s:

            if char in Open:
                stack.append(char)
            
            if char in Close:
                if not stack or stack[-1] != Close[char]:
                    return False
                else:
                    stack.pop()

        if stack:
            return False

        return True
