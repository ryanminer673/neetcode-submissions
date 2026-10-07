class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s_pre = ""

        s_lower = s.lower() 
        for c in s_lower:
            if c.isalnum():
                s_pre += c

        L = 0
        R = len(s_pre)-1

        while L < R:
            if s_pre[L] != s_pre[R]:
                return False
            L += 1
            R -= 1
        
        return True
