class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i, each in enumerate(stones):
            stones[i] = -1*each
        
        heapq.heapify(stones)
        
        while (len(stones) > 1):
            x = heapq.heappop(stones) * -1
            y = heapq.heappop(stones) * -1

            z = (x - y) * -1

            heapq.heappush(stones, z)

        return heapq.heappop(stones) * -1
        



            
        