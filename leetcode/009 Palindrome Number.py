'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
'''
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #496ms
        # temp=str(x)
        # l=len(temp)
        # left=0
        # right=l-1
        # while(right>=left):
        #     if temp[left]==temp[right]:
        #         left+=1
        #         right-=1
        #     else:
        #         return False
        # return True
        
        #340ms
        # if x < 0:
        #     return False
        # else:
        #     y = str(x)[::-1]
        #     if y == str(x):
        #         return True
        #     else: 
        #         return False

        #400ms
        if (x<0) or (x%10==0 and x!=0):
            return False
        rev_num=0
        while(x>rev_num):
            rev_num=rev_num*10+x%10
            x=x//10
        return ((x==rev_num) or (x==(rev_num//10)))