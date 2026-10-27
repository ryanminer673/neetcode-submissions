class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new_s_list = []
        for char in s:
            if char.isalpha() or char.isdigit():
                new_s_list.append(char.lower())

        new_s = "".join(new_s_list)

        l = 0
        r = len(new_s) - 1

        while l < r:
            if new_s[l] != new_s[r]:
                return False
            l += 1
            r -= 1

        return True
                