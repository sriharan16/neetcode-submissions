from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = defaultdict(int)
        
        for i in nums:
            c[i] += 1
        m = len(nums)/2

        for k,v in c.items():
            if v >= m:
                return k
