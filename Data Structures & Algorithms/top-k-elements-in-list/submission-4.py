from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d = defaultdict(int)

        for n in nums:
            d[n] += 1
        
        s_d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        l = list(s_d.keys())
        return l[:k]

        