class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        a = sum(ord(c) for c in s)
        b = sum(ord(c) for c in t)

        if a == b:
            return True
        return False
