class Solution:
    def isValid(self, s: str) -> bool:
        pair = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        stack = []
        for ch in s:
            if ch not in pair:
                stack.append(ch)
            else:
                if not stack or (stack.pop() != pair[ch]):
                    return False
        return len(stack) == 0