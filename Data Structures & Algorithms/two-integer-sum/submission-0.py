class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            pre = (target - num)
            if pre in seen:
                return [seen[pre],i]
            seen[num] = i