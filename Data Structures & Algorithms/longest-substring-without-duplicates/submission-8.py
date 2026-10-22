class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s)==1:
            return 1
        l = 0
        r = 0
        longest = 0

        subset = set()

        while r < len(s):

            if s[r] in subset:
                subset.remove(s[l])
                l += 1
            else:
                subset.add(s[r])
                r += 1
            longest = max(longest, len(subset))
        
        return longest

            
