class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dh = {}
        for i in range(len(nums)):
            df = target - nums[i]
            if df in dh:
                return [dh.get(df), i]
            else:
                dh[nums[i]] = i