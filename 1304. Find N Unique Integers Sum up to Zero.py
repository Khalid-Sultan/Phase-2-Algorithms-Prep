class Solution:
    def sumZero(self, n: int) -> List[int]:
        return [i for i in range(1, int(n/2)+1)] + [i for i in range(-1 * int(n/2), 0)] if n%2==0 else [i for i in range(1, int(n/2)+1)] + [i for i in range(-1 * int(n/2), 0)] + [0]