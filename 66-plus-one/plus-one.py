class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i=0
        carry=1
        while carry>0:
            carry+=digits[len(digits)-i-1]
            if(i>=len(digits)):
                digits=[carry]+digits
                return digits
            digits[len(digits)-i-1]=carry%10
            carry/=10
            i+=1
        return digits

                
        