class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return False
        i = 0
        j = 0

        k = 0

        while i < len(s) and j < len(t):
            if s[i] != t[j]:
                j += 1
            else:
                i += 1
                j += 1
                k += 1
                if k == len(s):
                    return True

        return False


        

        