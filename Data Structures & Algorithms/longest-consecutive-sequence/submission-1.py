class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        ls = 1
        s = 1
        if not nums:
            return 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                s += 1
            else:
                s = 1

            if ls < s:
                ls = s
        return ls
        