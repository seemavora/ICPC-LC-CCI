class Solution:
    def reverse(self, x: int) -> int:
        strInteger = str(x)
        if(strInteger[0] =='-'):
            strInteger = strInteger.replace('-','')
            reverseint = (strInteger[::-1])
            reverseint = '-' + reverseint
        else:
            reverseint = (strInteger[::-1])
        reverseint = int(reverseint)
        if(reverseint > 2**31-1 or reverseint<-2**31):
            return 0
        else:
            return reverseint