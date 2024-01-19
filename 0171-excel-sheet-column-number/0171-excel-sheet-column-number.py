class Solution:
    def dsf(self, n):
        tmp = n[0]
        if len(n) == 1:
            return ord(n) - ord('A') + 1
        return self.dsf(n[1:]) + (26**(len(n)-1) * (ord(tmp) - ord('A') + 1))
        
    def titleToNumber(self, columnTitle: str) -> int:
        return self.dsf(columnTitle)
        