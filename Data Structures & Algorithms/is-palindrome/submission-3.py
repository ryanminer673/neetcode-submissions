class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new_string = []
        for char in s:
            if char.isdigit() or char.isalpha():
                new_string.append(char.lower())

        sp = 0
        ep = len(new_string) - 1

        while ep >= 0:
            if new_string[sp] != new_string[ep]:
                return False
            sp += 1
            ep -= 1
        

        return True
                