class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        window = set()
        best = 0

        # we have a window of char
        # we move right 1 char
        # we check if that char is in the set
        # if it is then we remove from the left until that chatr is no langr in the set
        # the we add that char
        # the len of the set is teh window size


        for r in range(len(s)):

            while s[r] in window:
                window.remove(s[l])
                l += 1

            window.add(s[r])

            best = max(best, len(window))

            

        return best