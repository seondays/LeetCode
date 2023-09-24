class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        if target not in nums:
            return - 1

        while True:
            r = (end + start) // 2

            if nums[r] < target:
                start = r + 1
            elif nums[r] > target:
                end = r - 1
            else:
                return r