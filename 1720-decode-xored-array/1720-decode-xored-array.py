class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr=[first]
        r=0
        for i in range(1,len(encoded)+1):
            r=encoded[i-1]^arr[i-1]
            arr.append(r)
        return arr