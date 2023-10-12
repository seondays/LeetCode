class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def biToDe(binary):
            power = len(binary) - 1
            result = 0
            for i in binary:
                result += int(i) * (2 ** power)
                power -= 1
            return result

        def deToBi(decimal):
            result = ""
            if decimal == 0:
                return "0"
            while decimal > 0:
                result += str(decimal % 2)
                decimal = decimal // 2
            return result[::-1]
        
        return deToBi(biToDe(a)+biToDe(b))


        