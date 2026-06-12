class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        if not nums:
            return 

        maxi = nums[0]

        for i in range(n):
            total = 0
            for k in range(i+1,n):
                total += nums[k]

            maxi = max(maxi, total)

        return maxi


        