class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = nums[0]

        for i in range(n):
            total = 0  
            for j in range(i, n):
                total += nums[j]      
                maxi = max(maxi, total)

        return maxi