class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        nums.sort()
        return nums[-1] * nums[-2] - nums[1] * nums[0]