class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        freq_map = dict()

        for char in s:
            if char in freq_map:
                freq_map[char] += 1
            else:
                freq_map[char] = 1

        print(freq_map)

        for char in t:
            if char not in freq_map:
                return False
            else:
                if freq_map[char] == 1:
                    freq_map.pop(char)
                else:
                    freq_map[char] -= 1
        
        if freq_map:
            return False

        return True