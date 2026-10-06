class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        Sdict = dict()
        Tdict = dict()

        for i in range(len(s)):
            Sdict[s[i]] = 1 + Sdict.get(s[i], 0)
            Tdict[t[i]] = 1 + Tdict.get(t[i], 0)
        return Sdict == Tdict
