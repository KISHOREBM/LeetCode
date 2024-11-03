class Solution(object):
    def rotateString(self, s, goal):
        if len(s)!=len(goal):
            return False
        for i in range(len(goal)):
            if s[0]==goal[i]:
                k=(i+1)%len(goal)
                count=0
                for j in range(1,len(goal)):
                    if s[j]!=goal[k]:
                        break
                    k=(k+1)%len(goal)
                    count+=1
                if len(goal)==count+1:
                    return True
        return False




        