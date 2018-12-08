'''
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.
'''
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        flag=True
        ans=''
        for i in range(len(str)):
            if str[i] in '0123456789':
                ans+=str[i]
                flag=False
            elif str[i]==' ':
                if flag==True:
                    continue
                else:
                    break
            elif str[i] in '+-':
                if flag==True:
                    ans+=str[i]
                    flag=False
                else:
                    break
            else:
                break
        if flag==True:
            ans='0'
        else:
            if ans[0]=='+':
                if len(ans)>1:
                    ans=ans[1:len(ans)]
                else:
                    ans='0'
            elif ans[0]=='-':
                if len(ans)==1:
                    ans='0'
        ans=int(ans)
        if ans<(-pow(2,31)):
            return (-pow(2,31))
        elif ans>(pow(2,31)-1):
            return (pow(2,31)-1)
        else:
            return ans