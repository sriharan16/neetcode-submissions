from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # d = defaultdict(int)
        d = {}
        for i,n in enumerate(nums):
            if d.get(n) is not None:
                return [d[n], i]
            d[target-n] = i
        # return 


        