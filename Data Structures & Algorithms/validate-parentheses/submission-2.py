class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for each in s:
            if each == "}":
                if not stack or stack.pop() != "{":
                    return False
            elif each == "]":
                if not stack or stack.pop() != "[":
                    return False
            elif each == ")":
                if not stack or stack.pop() != "(":
                    return False
            else:
                stack.append(each)
        return not stack