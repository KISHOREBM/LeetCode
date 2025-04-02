class Solution(object):
    def divide(self, dividend, divisor):
        if dividend ==-2147483648 and divisor==-1:
            return 2147483647
        negative = (dividend < 0) ^ (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        remainder = 0
        bits = dividend.bit_length()

        for i in range(bits):  
            remainder = (remainder << 1) | ((dividend >> (bits - 1 - i)) & 1)
            if remainder >= divisor:  
                remainder -= divisor
                quotient = (quotient << 1) | 1
            else:
                quotient = quotient << 1

        return -quotient if negative else quotient
