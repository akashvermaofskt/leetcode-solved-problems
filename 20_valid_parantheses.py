from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        opening = set({"(", "{", "["})
        closing = set({")", "}", "]"})
        for c in s:
            if c in opening:
                stack.append(c)
            elif c in closing and len(stack) > 0 and stack[-1] in opening:
                if (
                    (c == ")" and stack[-1] != "(")
                    or (c == "}" and stack[-1] != "{")
                    or (c == "]" and stack[-1] != "[")
                ):
                    return False
                else:
                    stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        return False


print(Solution.isValid(Solution, "(]"))
