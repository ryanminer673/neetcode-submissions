class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        p1 = 0
        p2 = 0

        seen = set()

        best = 0

        while p2 < len(s):
            if s[p2] in seen:
                seen.remove(s[p1])
                p1 += 1
            else:
                seen.add(s[p2])
                p2 += 1

            best = max(p2 - p1, best)

        return best

