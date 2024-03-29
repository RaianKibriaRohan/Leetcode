class Solution(object):
    def romanToInt(self, s):
        store = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        sum = 0
        prev_value = 0
        for i in s[::-1]:
            curr_value = store[i]
            if curr_value < prev_value:
                sum -= curr_value  
            else:
                sum += curr_value
            prev_value = curr_value
            
        return sum


call1 = Solution()
call1.romanToInt("III")

call2 = Solution()
call2.romanToInt("LVIII")

call3 = Solution()
call3.romanToInt("MCMXCIV")
        