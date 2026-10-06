class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        store = dict()

        for char in s:
            if char in store:
                store[char] += 1
            else:
                store[char] = 1
        
        for char in t:
            if char not in store:
                return False

            if store[char] == 1:
                store.pop(char)
            else:
                 store[char] -= 1

        if store:
            return False
        else:
            return True



