class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        valid_open_parenthisis = {'[', '(', '{'}
        valid_close_parenthisis = {']', ')', '}'}
        valid_parenthisis = {']': '[', ')': '(', '}': '{'}


        for char in s:
            if char in valid_open_parenthisis:
                stack.append(char)
            elif char in valid_close_parenthisis and stack and stack[-1] == valid_parenthisis[char]:
                stack.pop()
            else:
                return False
        
        if stack:
            return False
        else:
            return True
