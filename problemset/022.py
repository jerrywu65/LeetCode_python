'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        def backtrack(s='',left=0,right=0):
            if len(s)==2*n:
                return res.append(s)
            if left<n:
                backtrack(s+'(',left+1,right)
            if right<left:
                backtrack(s+')',left,right+1)
        backtrack()
        return res