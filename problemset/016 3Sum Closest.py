'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''
###132ms
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res=nums[0]+nums[1]+nums[2]
        temp=abs(nums[0]+nums[1]+nums[2]-target)
        if temp==0:
            return target
        else:
            for i in range(len(nums)):
                left=i+1
                right=len(nums)-1
                
                if i>0 and nums[i-1]==nums[i]:
                    continue

                while left<right:
                    sum=nums[i]+nums[left]+nums[right]
                    if abs(sum-target)<temp:
                        temp=abs(sum-target)
                        res=sum
                    
                    if sum<target:
                        left+=1
                    elif sum>target:
                        right-=1
                    
                    if temp==0:
                        return target
                    if left>1:
                        while left<right and nums[left-1]==nums[left]:
                            left+=1
                    if right<len(nums)-1:
                        while left<right and nums[right+1]==nums[right] :
                            right-=1
            return res