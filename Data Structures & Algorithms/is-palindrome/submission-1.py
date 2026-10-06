class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ""
        for each in s:
            if each.isalpha() or each.isdigit():
                s2 += each.lower()
        return s2 == s2[::-1]