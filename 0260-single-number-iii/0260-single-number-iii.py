class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n=len(nums)
        r=0
        
        for i in nums:
            r=r^i
        d=r & -r
        a=0
        b=0
        for i in nums:
            if i&d:
                a=a^i
            else:
                b=b^i
        return [a,b]