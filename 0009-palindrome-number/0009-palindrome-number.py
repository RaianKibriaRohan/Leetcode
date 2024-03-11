class Solution(object):
    def isPalindrome(self, x):
        con = str(x)
        rev = ''
        initial = 0
        for i in range(len(con)-1,-1,-1):
            if i>=initial:
                rev+=con[i]
            else:
                break
        if rev==con:
            return True
        else:
            return False

call1 = Solution()
call1.isPalindrome(121)

call2 = Solution()
call2.isPalindrome(-121)

call3 = Solution()
call3.isPalindrome(10)



        