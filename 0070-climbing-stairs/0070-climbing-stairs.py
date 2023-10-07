class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        
        before, now = 0, 1

        for i in range(n):
            tmp = before
            before = now
            now = now + tmp
        return now

        