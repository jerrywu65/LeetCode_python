'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ans=[]
        temp=[]
        for i in range(len(nums)):
            if i>0 and nums[i-1]==nums[i]:
                continue
            for j in range(i+1,len(nums)):
                if j>i+1 and nums[j-1]==nums[j]:
                    continue
                
                left=j+1
                right=len(nums)-1
                
                while left<right:
                    sum=nums[i]+nums[j]+nums[left]+nums[right]
                    if sum==target:
                        temp=[nums[i],nums[j],nums[left],nums[right]]
                        ans.append(temp)
                        left+=1
                        right-=1

                        while left<right and nums[left-1]==nums[left]:
                            left+=1
                        while left<right and nums[right+1]==nums[right]:
                            right-=1
                    elif sum<=target:
                        left+=1
                    else:
                        right-=1
        return ans