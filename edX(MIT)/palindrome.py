def isPalindrome(s):
    def isChar(s):
        s=s.lower()
        ans =''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwzxy':
                ans=ans+c
        return ans
    def isPali(s):
        if len(s)<=1:
            return True
        else:
            return s[0]==s[-1] and isPali(s[1:-1])
    return isPali(isChar(s))
print (''+str(isPalindrome('la')))
