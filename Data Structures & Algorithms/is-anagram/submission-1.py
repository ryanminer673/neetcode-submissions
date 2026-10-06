class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        D = {}
        for i in range(len(s)):
            char = s[i]
            if char in D:
                D[char] += 1
            else:
                D[char] = 1

        for i in range(len(t)):
            char = t[i]
            if char in D:
                if D[char] == 1:
                    del D[char]
                else:
                    D[char] -= 1
            else:
                return False

        if not D:
            return True
        else:
            return False

