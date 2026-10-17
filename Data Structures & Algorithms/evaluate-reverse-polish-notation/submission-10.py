class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for char in tokens:
            if len(char) > 0 and char[0] == '-' and char[1:].isdigit():
                stack.append(int(char[1:]) * -1)
            if char.isdigit():
                stack.append(int(char))
            else:
                if char == '+':
                    x = stack.pop()
                    y = stack.pop()
                    stack.append(x + y)
                elif char == '-':
                    x = stack.pop()
                    y = stack.pop()
                    stack.append(y - x)
                elif char == '*':
                    x = stack.pop()
                    y = stack.pop()
                    stack.append(x * y)
                elif char == '/':
                    x = stack.pop()
                    y = stack.pop()
                    stack.append(int(y/x))
        return stack[0]
            