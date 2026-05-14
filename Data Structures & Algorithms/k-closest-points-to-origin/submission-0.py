class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d = []

        for point in points:
            x = point[0]
            y = point[1]

            dist = x*x + y*y

            heapq.heappush(d, (dist,point))

        ans = []

        for i in range(len(d)):
            if i == k:
                break
            val = heapq.heappop(d)
            ans.append(val[1])

        return ans
