class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = set()
        i, j = 0, 0

        n = len(s)
        long = 0

        while j < n:
            if s[j] not in res:
                res.add(s[j])
                j += 1
                long = max(long, j -i)
            else:
                res.remove(s[i])
                i += 1

        return long

            
            
        