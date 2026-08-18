class Solution:
    def findComplement(self, num: int) -> int:
        if num==0:
            bs="0"
        else:
            bs=""
            while num>0:
                a=str(num%2)
                if a=='0':
                    a='1'
                else:
                    a='0'
                bs=a+bs
                num=num//2
        ans=int(bs,2)
        return ans