class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        sorted_nums = sorted(nums)
        smaller_count = {}
        for i, num in enumerate(sorted_nums):
            if num not in smaller_count:
                smaller_count[num] = i
        return [smaller_count[num] for num in nums]