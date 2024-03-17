class Solution(object):
    def removeDuplicates(self, nums):
        temp = [None]
        count = 0
        for i in range(0, len(nums)):
            if nums[i]==temp[0]:
                nums[i] = '_'
                continue
            temp = [None]
            if temp[0]==None:
                temp[0] = nums[i]

        nums.sort()   
        for i in nums:
            if type(i)==int:
                count+=1
    
        return count
        