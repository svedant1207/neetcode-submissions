class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = 0
        maxie = 0

        for i in range(n):
            if i % 2 ==0:
                maxi += nums[i]
            else:
                maxie += nums[i]


        return max(maxi, maxie)


        