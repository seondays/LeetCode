class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        s = s + " "

        for i in range(len(s)-1):
            c = s[i]
            next_c = s[i+1]

            if c == "I":
                if next_c == "V" or next_c == "X":
                    result -= 1
                else:
                    result += 1
            if c == "V":
                result += 5
            if c == "X":
                if next_c == "L" or next_c == "C":
                    result -= 10
                else:
                    result += 10
            if c == "L":
                result += 50
            if c == "C":
                if next_c == "D" or next_c == "M":
                    result -= 100
                else:
                    result += 100
            if c == "D":
                result += 500
            if c == "M":
                result += 1000
        
        return result