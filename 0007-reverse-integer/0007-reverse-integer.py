class Solution(object):
    def reverse(self, x):
        new = ''
        operators = ['+', '-']  
        con = str(x)
        if con[0] in operators:
            new+=con[0]

        for i in range(len(con)-1,-1,-1):
            if con[i]==0:
                continue
            elif con[i] in operators:
                break
            else:
                new+=con[i]
        
        if -2**31<=int(new)<=2**31-1:
            return int(new)
        else:
            return 0
        

call1 = Solution()
call1.reverse(123)

call2 = Solution()
call2.reverse(-123)

call3 = Solution()
call3.reverse(120)
