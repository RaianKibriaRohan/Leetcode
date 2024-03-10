class Solution(object):
    def intersection(self, nums1, nums2):
        new = []
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                if nums1[i] not in new:
                    new.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return new
        
call1 = Solution()
call1.intersection([1,2,2,1], [2,2])

call2 = Solution()
call2.intersection([4,9,5], [9,4,9,8,4])