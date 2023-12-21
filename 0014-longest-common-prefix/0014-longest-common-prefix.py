class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        index = 0

        while index < len(strs[0]):
            character = strs[0][index]
            for word in strs:
                if index >= len(word) or word[index] != character:
                    return result
            result += character
            index += 1
        return result