class Solution(object):
    def reverseString(self, s):
        c = 0
        for i in range(len(s)-1,-1,-1):
            if c<i:
                taking_front = s[c]
                taking_back = s[i]
                s[c] = taking_back
                s[i] = taking_front
                c+=1
            else:
                pass
        return s
        