class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}

        for i in range(len(s)):
            if s[i] in dict:
                dict[s[i]] += 1
            else:
                dict[s[i]] = 1
        
        for i in range(len(t)):
            if t[i] in dict:
                dict[t[i]] -= 1
            else:
                return False
        
        for i in dict.values():
            if i != 0:
                return False
        
        return True