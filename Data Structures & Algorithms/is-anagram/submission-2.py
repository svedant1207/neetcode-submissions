class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        check = list(s)

        for c in t:
            if c in check:
                check.remove(c)
            else:
                return False
        return len(check) == 0