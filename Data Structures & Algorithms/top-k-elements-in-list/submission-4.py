class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_map = {}

        # O(n)
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        
        #O(n)
        freq_list = []
        for key, value in freq_map.items():
            freq_list.append(((-1 * value), key))

        #O(n)
        heapq.heapify(freq_list)
        
        result = []

        while k > 0:
            freq, num = heapq.heappop(freq_list)
            result.append(num)
            k-=1

        return result