class Solution(object):
    def longestCommonPrefix(self, strs):
        ret=strs[0]
        c=len(ret)
        for i in strs[1:]:
            count=0
            for j in range(len(i)):
                if j<len(i) and j < len(ret) and i[j]==ret[j]:
                    count+=1
                else:
                    break
            if count<c:
                c=count
        return ret[:c]

        