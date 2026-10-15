class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        seen = {}

        for char in s:
            if char in seen:
                seen[char] += 1
            else:
                seen[char] = 1

        for char in t:
            if char in seen:
                if seen[char] == 1:
                    seen.pop(char)
                else:
                    seen[char] -= 1
            else:
                return False

        if seen:
            return False
        else:
            return True


