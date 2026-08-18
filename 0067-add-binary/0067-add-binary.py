class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i=len(a)-1
        j=len(b)-1
        c=0
        res=""
        while i>=0 or j>=0 or c!=0:
            if i>=0:
                x=int(a[i])
            else:
                x=0
            if j>=0:
                y=int(b[j])
            else:
                y=0
            s=x+y+c
            res=str(s%2)+res
            c=s//2
            i-=1
            j-=1
        return res