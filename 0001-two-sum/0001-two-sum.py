class Solution(object):
    def twoSum(self, nums, target):
        final = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    final.append(i)
                    final.append(j)
                    break
                else:
                    continue
        return final

call1 = Solution()
call1.twoSum([2,7,11,15], 9)

call2 = Solution()
call2.twoSum([3,2,4], 6)

call3 = Solution()
call3.twoSum([3,3], 6)

        