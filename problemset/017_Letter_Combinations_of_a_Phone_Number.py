'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

{'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
'''
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        map={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        l=len(digits)
        ans=[]
        if len(digits)==0:
            return []
        elif len(digits)==1:
            for i in map[digits[0]]:
                ans.append(i)
        else:
            ans.append('')#用来使comnibe函数的 list循环开始
            for i in range(l):
                ans=self.combine(map[digits[i]],ans)                
            
        return ans
    
    def combine(self,str,list):
        res=[]
        for j in str:
            for i in list:
                res.append(i+j)
        return res