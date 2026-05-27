from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l < r:

            mid = l + (r-l)//2

            hour = 0

            for pile in piles:
                hour += ceil(pile/mid)

            if hour <= h:
                r = mid
            else:
                l = mid + 1

        return l

            

        