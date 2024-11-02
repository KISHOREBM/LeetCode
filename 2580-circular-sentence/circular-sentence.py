class Solution(object):
    def isCircularSentence(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        ret=sentence.split()
        # if(len(ret)==1):
        #     return True
        for i in range(len(ret)):
            if ret[i][-1]!=ret[(i+1)%len(ret)][0]:
                # print(ret[i][-1],ret[i],ret[i+1],ret[(i+1)%len(ret)][0])
                return False
        return True
        