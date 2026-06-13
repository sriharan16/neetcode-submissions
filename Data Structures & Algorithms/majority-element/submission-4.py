from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
        maj = 0
        num = None
        print(counts)
        for n,s in counts.items():
            if s > maj:
                num = n
                maj = s
            # if len(nums)//2 < num:
            #     break
        return num


        