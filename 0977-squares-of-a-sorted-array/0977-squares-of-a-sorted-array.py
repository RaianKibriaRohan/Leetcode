class Solution(object):
    def sortedSquares(self, nums):
        new = []
        for i in nums:
            new.append(i**2)
        new.sort()
        return new

call1 = Solution()
call1.sortedSquares([-4, -1, 0, 3, 10])
call2 = Solution()
call2.sortedSquares([-7, -3, 2, 3, 11])

