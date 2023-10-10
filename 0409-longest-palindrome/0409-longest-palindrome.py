class Solution:
    def longestPalindrome(self, s: str) -> int:
        palindrome = {}
        result = 0
        one = True

        for i in range(len(s)):
            if s[i] not in palindrome:
                palindrome[s[i]] = 1
            else:
                palindrome[s[i]] += 1
        
        for i in palindrome.values():
            if i % 2 == 0:
                result += i
            if i % 2 != 0:
                if one:
                    result += i
                    one = False
                else:
                    result += (i-1)
        
        return result

            
        