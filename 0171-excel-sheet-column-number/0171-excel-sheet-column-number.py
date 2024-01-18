class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for digit in columnTitle:
            result = result * 26 + ord(digit) - 64
        return result