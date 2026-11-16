class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #O(n)
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 0 

        #O(N)
        heap = []
        for key, value in freq_map.items():
            heap.append((-1 * value, key))

        #O(N)
        heapq.heapify(heap)

        #O(KLogN)
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])

        return result

