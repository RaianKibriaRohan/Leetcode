class Solution(object):
    def missingNumber(self, nums):
        temp = len(nums)
        for i in range(len(nums)):
            temp+=(i-nums[i])
        return temp
        