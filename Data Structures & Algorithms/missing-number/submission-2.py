class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor_s = n

        for i in range(n):
            xor_s = xor_s ^ i ^ nums[i]

        return xor_s