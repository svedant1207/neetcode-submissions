class Solution:
    def isValid(self, s: str) -> bool:
        m = {
            '[': ']',
            '(': ')',
            '{': '}'
        }
        stk = []

        for i in s:
            if i in m:
                stk.append(i)
            else:
                if not stk:
                    return False
                a = stk.pop()
                if m[a] != i:
                    return False

        return True