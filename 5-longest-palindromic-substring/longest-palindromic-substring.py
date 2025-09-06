class Solution(object):
    def longestPalindrome(self, s):
        
        ret=""
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                st=s[i:j+1]
                # print(st)
                if st == st[::-1] and len(st)>len(ret):
                    ret=st
        return ret if len(ret)>1 else s[0]
        