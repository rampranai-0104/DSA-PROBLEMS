class Solution:
    def addDigits(self, num: int) -> int:
        s=0
        while num>0:
            r=num%10
            s+=r
            num=num//10
        if s>9:
            return self.addDigits(s)
        else:
            return s