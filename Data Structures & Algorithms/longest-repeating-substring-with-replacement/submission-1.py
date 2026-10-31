class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        window_map = {}
        best = 0

        for right in range(len(s)):

            if s[right] in window_map:
                window_map[s[right]] += 1
            else:
                window_map[s[right]] = 1

            total = 0
            most = 0
            for value in window_map.values():
                total += value
                most = max(most, value)


            while (total - most) > k:

                if window_map[s[l]] == 1:
                    window_map.pop(s[l])
                else:
                    window_map[s[l]] -= 1

                l += 1 

                total = 0
                most = 0
                for value in window_map.values():
                    total += value
                    most = max(most, value)

            best = max(best, total)

        return best