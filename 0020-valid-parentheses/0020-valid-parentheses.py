class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if x == '(' or x == '{' or x == '[':
                stack.append(x)
            else:
                if len(stack) == 0:
                    return False
                if stack[-1] == '(' and x == ')':
                    stack.pop()
                elif stack[-1] == '{' and x == '}':
                    stack.pop()
                elif stack[-1] == '[' and x == ']':
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False