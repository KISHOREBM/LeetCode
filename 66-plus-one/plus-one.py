class Solution(object):
    def plusOne(self, digits):
        j=len(digits)-1
        carry=0
        while j>=0:
            if digits[j]+1>=10:
                carry=1
                digits[j]=0
                j-=1
            else:
                digits[j]+=1
                carry=0
                break
        # print(digits)
        if carry==1:
            digits.insert(0,carry)
        return digits
        # while j>=0:
        #     if digits[j]<9:
        #         digits[j]+=1
        #         return digits
        #     digits[j]=0
        #     j-=1
        # return [1]+digits



            
        