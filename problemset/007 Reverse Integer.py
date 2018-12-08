'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ####72ms
        # temp=0
        # ans=0
        # if (x<(0-pow(2,31))) or (x>(pow(2,31)-1)):
        #     ans=0
        # if x==0:
        #     ans=0
        # elif x>0:
        #     while(x>0):
        #         temp=x%10
        #         ans=10*ans+temp
        #         x=x//10
        # else:
        #     x=abs(x)
        #     while(x>0):
        #         temp=x%10
        #         ans=10*ans+temp
        #         x=x//10
        #     ans=0-ans
        # #减测反转后是否超出范围
        # if (ans<0-pow(2,31)) or (ans>(pow(2,31)-1)):
        #     return 0
        # return ans
        
        ###64ms
        if (x<(0-pow(2,31))) or (x>(pow(2,31)-1)):
            ans=0
        if x>=0:
            x=str(x)
            x=list(x)
            x.reverse()
            ans=''.join(x)
        else:
            x=abs(x)
            x=str(x)
            x=list(x)
            x.reverse()
            ans=''.join(x)
            ans='-'+ans
        #检测反转后是否在范围内
        if ans[0]=='-':
            if len(ans)<11:
                return int(ans)
            elif len(ans)>11:
                return 0
            else:
                a=ans[1:len(ans)]
                temp=str(pow(2,31))
                if a>temp:
                    return 0
                else:
                    return int(ans)
        else:
            if len(ans)<10:return int(ans)
            elif len(ans)>10:return 0
            else:
                temp=str(pow(2,31)-1)
                if ans>temp:
                    return 0
                else:
                    return int(ans)