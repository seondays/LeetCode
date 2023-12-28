class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        tmp = int(''.join([str(i) for i in digits])) + 1
        return [int(n) for n in str(tmp)]