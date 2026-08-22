class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n=len(nums)
        f={}
        r=0
        for i in range(n):
            if nums[i] not in f:
                f[nums[i]]=1
            else:
                f[nums[i]]+=1
        for i in f:
            if f[i]==1:
                r=i
        return r