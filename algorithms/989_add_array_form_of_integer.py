class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        A = int("".join(str(x) for x in A))
        return list(str(A + K))
