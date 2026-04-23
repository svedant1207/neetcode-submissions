class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}

        for idx, num in enumerate(nums):
            pre = target - num
            if pre in s:
                return [s[pre], idx]
            s[num] = idx
        
            
