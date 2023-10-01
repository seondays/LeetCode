# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if (not isBadVersion(n - 1)) and isBadVersion(n):
            return n
        versions = (1 + n) // 2
        while not isBadVersion(versions):
            versions = (n + versions) // 2
        
        if (not isBadVersion(versions - 1)) and isBadVersion(versions):
            return versions
        else:
            return self.firstBadVersion(versions)