class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # window is valid when no duplicate chars
        # window invalid when duplicate, move left (poping left char) until its = right 
        # or until no dups in set

        # start with empty window
        #check if adding r ruins it 
        # if it does then i pop left until it doesnt 
        # then i add right

        left = 0
        window = set()
        best = 0

        for right in range(len(s)):

            #checks if adding the new char breaks valid window cond
            # move left until teh adding right is ok
            while s[right] in window:
                window.remove(s[left])
                left += 1

            # now add right and i know uts valid
            window.add(s[right])

            best = max(best, len(window))

        return best

            