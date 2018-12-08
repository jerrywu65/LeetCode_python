'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
'''
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans=''
        num=len(strs)
        flag=False
        if len(strs)==0:
            return ans
        elif len(strs)==1:
            return strs[0]
        else:
            min_len=len(strs[0])
            for i in range(num):
                if len(strs[i])<min_len:
                    min_len=len(strs[i])
            for i in range(min_len):
                for j in range(num-1):
                    if strs[j][i]==strs[j+1][i]:
                        flag=True
                    else:
                        flag=False
                        break
                if flag==True:
                    ans+=strs[0][i]
                else:
                    break
            return ans