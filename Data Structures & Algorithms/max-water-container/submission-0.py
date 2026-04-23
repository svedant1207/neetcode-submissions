class Solution:
    def maxArea(self, hs: List[int]) -> int:
        n = len(hs)
        l = 0
        r = n -1
        best = 0

        while l < r:
            w = r - l
            h = min(hs[l], hs[r])
            a = h * w
            best = max(best, a)

            if hs[l] < hs[r]:
                l += 1
            else:
                r -= 1

        return best







        