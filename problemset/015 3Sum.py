'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans=[]
        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1
            
            if i>0 and nums[i-1]==nums[i]:
                continue
            '''
            用来代替
            if temp not in ans:
                ans.append(temp)
            否则会超时
            '''
            while left<right:
                sum=nums[i]+nums[left]+nums[right]
                if sum==0:
                    temp=[nums[i],nums[left],nums[right]]
                    ans.append(temp)
                    left+=1
                    right-=1
                    
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                    
                elif sum<0:
                    left+=1
                else:
                    right-=1
        return ans