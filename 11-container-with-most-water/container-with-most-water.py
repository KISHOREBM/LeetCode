class Solution(object):
    def maxArea(self, height):
        left=0
        right=len(height)-1
        area=0
        while(right>left):
            pre=min(height[left],height[right])*(right-left)
            if height[left]>height[right]:
                right-=1
            else:
                left+=1
            if pre>area:
                area=pre
        return area
        