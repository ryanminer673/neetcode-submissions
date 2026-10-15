class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_map = {}

        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        
        heap = []

        for key, value in freq_map.items():
            heapq.heappush(heap, (-1 * value, key))

        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
 
        return result

        