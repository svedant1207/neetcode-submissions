class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        buck = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for num, v in count.items():
            buck[v].append(num)

        res = []

        for i in range(len(buck)-1,0,-1):
            for f in buck[i]:
                res.append(f)
                if len(res) == k:
                    return res


