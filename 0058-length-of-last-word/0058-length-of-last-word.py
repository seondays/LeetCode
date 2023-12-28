class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = 0
        for word in s.strip()[::-1]:
            if word.isspace():
                break
            result += 1
        return result
            