class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        pairs = {
                ')' : '(',
                ']' : '[',
                '}' : '{'
        }
        for b in s:
            if b in pairs:
                if not stk or stk[-1] != pairs[b]:
                    return False
                stk.pop()
            else:
                stk.append(b)
        return len(stk) == 0