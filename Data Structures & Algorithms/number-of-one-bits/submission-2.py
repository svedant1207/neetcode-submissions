class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        mask = 1

        for i in range(64):
            count += n & (mask << i) != 0

        return count


        