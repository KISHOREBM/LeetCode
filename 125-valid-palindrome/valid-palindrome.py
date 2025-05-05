class Solution(object):
    def isPalindrome(self, s):
        s=s.lower()
        s=''.join([i for i in s if i.isalnum()])
        if s!=s[::-1]:
            return False
        return True
        