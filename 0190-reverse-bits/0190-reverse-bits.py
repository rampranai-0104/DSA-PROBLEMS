class Solution:
    def reverseBits(self, n: int) -> int:
        c=f"{n:032b}"
        p=c[::-1]
        return int(p,2)