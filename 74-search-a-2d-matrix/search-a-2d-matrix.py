class Solution(object):
    def searchMatrix(self, matrix, target):
        for i in matrix:
            if i[-1]>=target:
                for i in i:
                    if i==target:
                        return True
        return False
        