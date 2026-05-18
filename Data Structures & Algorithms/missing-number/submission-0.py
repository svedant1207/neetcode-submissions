class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        for i in range(nums[-1]):
            if nums[i] ^ i == 0:
                continue
            else:
                return i