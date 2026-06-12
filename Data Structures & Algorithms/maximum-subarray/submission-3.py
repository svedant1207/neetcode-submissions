class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        currs = nums[0]
        maxs = nums[0]

        for n in nums[1:]:

            currs = max(n, currs + n)

            maxs = max(maxs, currs)

        return maxs