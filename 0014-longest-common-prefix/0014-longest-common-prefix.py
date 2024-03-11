class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        first_str_len = len(strs[0])

        for i in range(first_str_len):
            char = strs[0][i]

            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != char:
                    return strs[0][:i]

        return strs[0] 


call1 = Solution()
call1.longestCommonPrefix(["flower","flow","flight"])

call2 = Solution()
call2.longestCommonPrefix(["dog","racecar","car"])