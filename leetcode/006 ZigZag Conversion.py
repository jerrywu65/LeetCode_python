'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:
'''
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        l=len(s)
        ans=''
        temp=2*numRows-2
        # index=0
        for i in range(numRows):
            j=0
            while (i+j)<l:
                ans+=s[j+i]
                if (i!=0) and (i!=numRows-1):
                    if (j+temp-i)<l:
                        ans+=s[j+temp-i]
                j+=temp
        return ans
                    