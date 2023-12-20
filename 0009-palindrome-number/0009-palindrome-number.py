class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev_x = str(x)[::-1]

        if rev_x == str(x) :
            return True
        return False