class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        zc = 0
        for n in nums:
            if n:
                p *= n
            else:
                zc += 1
        if zc > 1:
            return [0] * len(nums)
        
        res = [0] * len(nums)
        for i,n in enumerate(nums):
            if zc:
                res[i] = 0 if n else p
            else:
                res[i] = int(p // n)
        return res
        