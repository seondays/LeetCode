class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        standard = len(nums) / 2
        d = {}

        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        
        for k,v in d.items():
            if v > standard:
                return k