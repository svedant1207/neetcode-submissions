class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = {}

        for i in s:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1

        for i in t:
            if i in a:
                a[i] -= 1
            else:
                return False

        for i in a.values():
            if i != 0:
                return False
        return True
        