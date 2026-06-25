class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ']': '[',
            ')': '(',
            '}': '{'
        }

        stack = []

        for i in range(len(s)):
            if s[i] not in pairs:
                stack.append(s[i])
            else:
                if len(stack) and stack.pop() == pairs[s[i]]:
                    pass
                else:
                    return False
        
        return len(stack) == 0
                