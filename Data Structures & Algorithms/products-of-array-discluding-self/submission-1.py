class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_n = [0] * n
        right_n = [0] * n
        left_p = 1
        right_p = 1

        for i in range(n):
            j = -i-1

            left_n[i] = left_p
            right_n[j] = right_p
            left_p *= nums[i]
            right_p *= nums[j]

        return [l*r for l,r in zip(left_n,right_n)]