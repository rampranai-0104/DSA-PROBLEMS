class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        m=len(s)
        n=len(t)
        f={}
        r=""
        for i in range(m):
            if s[i] not in f:
                f[s[i]]=1
            else:
                f[s[i]]+=1
        for i in range(n):
            if t[i] in f:
                f[t[i]]-=1
                if f[t[i]]==-1:
                    r=t[i]
            else:
                r=t[i]
        return r