'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
'''
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def center(s,left,right):
            L=left
            R=right
            # while((L>=0) and (R<len(s)) and (s[L]==s[R])):
            #     L--
            #     R++
            while (L>=0 and R<len(s)):
                if s[L]==s[R]:
                    L-=1
                    R+=1
                else:
                    break
            return R-L-1
        # if len(s)<1:
        #     return ''
        start=0
        end=0
        for i in range(len(s)):
            len1=center(s,i,i)
            len2=center(s,i,i+1)
            length=max(len1,len2)
            if (length>end-start):
                start=i-(length-1)//2
                end=i+length//2
        return s[start:end+1]