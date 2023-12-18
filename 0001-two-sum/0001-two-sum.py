class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}

        for i in range(len(nums)):
            sub = target - nums[i]
            if sub in result:
                return [result[sub],i]
            result[nums[i]] = i
        return []