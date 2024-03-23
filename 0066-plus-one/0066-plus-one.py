class Solution(object):
    def plusOne(self, digits):
        temp = ''
        final = []
        for i in digits:
            temp+=str(i)
        temp = int(temp)+1
        
        for j in str(temp):
            final.append(int(j))
            
        return final
        