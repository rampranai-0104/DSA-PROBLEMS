class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=[[]]
        for i in nums:
            s=len(res)
            for j in range(s):
                ns=[]
                for y in res[j]:
                    ns.append(y)
                ns.append(i) 
                res.append(ns)
        return res       