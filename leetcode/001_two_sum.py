'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)<2:
            return ([-1,-1])
        else:
            for i in range(0,len(nums)):
                for j in range(i+1,len(nums)):
                    if nums[i]+nums[j]==target:
                        return (i,j)
        
                        
        