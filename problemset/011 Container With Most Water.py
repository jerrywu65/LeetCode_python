'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
'''
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area=0
        left=0
        right=len(height)-1
        while(right>left):
            if height[left]>height[right]:
                h=height[right]
                right-=1
            else:
                h=height[left]
                left+=1
            s=h*(right-left+1)
            if s>max_area:
                max_area=s
        return max_area