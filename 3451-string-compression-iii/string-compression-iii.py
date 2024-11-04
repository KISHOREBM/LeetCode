class Solution(object):
    def compressedString(self, word):
        """
        :type word: str
        :rtype: str
        """
        ret=""
        count=0
        i=0
        while i<len(word):
            j=i
            while(j<len(word) and word[i]==word[j] and count<9):
                count+=1
                j+=1
            ret=ret+"{}{}".format(count,word[i])
            count=0
            i=j
        return ret
                
        