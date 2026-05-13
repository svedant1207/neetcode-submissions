class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [-stone for stone in stones]

        heapq.heapify(stones)

        while len(stones) > 1:

            largest = -heapq.heappop(stones)
            second_l = -heapq.heappop(stones)

            smash = largest - second_l

            if smash != 0:
                heapq.heappush(stones, -smash)
        
        if not stones:
            return 0

        return -stones[0]


        