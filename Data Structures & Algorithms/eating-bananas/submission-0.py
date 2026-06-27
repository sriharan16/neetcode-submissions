class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # math.ceil(float(p) / k)

        l = 1
        r = max(piles)
        k = r

        while (l<= r):
            # print(l, r)
            m = l + (r-l)//2
            tt = 0
            for p in piles:
                tt += math.ceil(float(p) / m)
            if tt <= h:
                k = m
                r = m-1
            else:
                l = m+1
        return k


