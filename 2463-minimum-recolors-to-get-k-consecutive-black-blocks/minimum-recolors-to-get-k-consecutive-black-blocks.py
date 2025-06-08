class Solution(object):
    def minimumRecolors(self, blocks, k):
        if len(blocks)==k:
            return blocks.count('W')
        recolor=0
        res=k
        for i in range(len(blocks)):
            if i<k:
                if blocks[i]=='W':
                    recolor+=1
            else:
                res=min(res,recolor)
                if blocks[i]=='W':
                    recolor+=1
                if blocks[i-k]=='W':
                    recolor-=1
        return min(res,recolor)
        