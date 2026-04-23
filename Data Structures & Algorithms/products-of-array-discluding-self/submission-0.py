class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l_prod = 1
        r_prod = 1
        l_arr = [0]*n
        r_arr = [0]*n

        for i in range(n):
            j = -i-1

            l_arr[i] = l_prod
            r_arr[j] = r_prod

            l_prod *= nums[i]
            r_prod *= nums[j]
        
        return [l*r for l,r in zip(l_arr,r_arr)]

        