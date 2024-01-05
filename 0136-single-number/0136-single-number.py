class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        holder = {}
        for number in nums:
            if number in holder:
                holder[number] += 1
            else:
                holder[number] = 1
        for k,v in holder.items():
            if v == 1:
                return k