class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_map = {}

        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        freq_to_value = {}

        for num, freq in freq_map.items():
            if freq in freq_to_value:
                freq_to_value[freq].append(num)
            else:
                freq_to_value[freq] = [num]

        result = []

        for i in range(len(nums), 0, -1):
            if i in freq_to_value:
                for num in freq_to_value[i]:
                    if k != 0:
                        result.append(num)
                        k -= 1
                if k == 0: 
                    break

 
        return result

        