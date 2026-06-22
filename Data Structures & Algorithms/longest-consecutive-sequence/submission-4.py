class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)

        longest = 0

        for num in numset:
            if (num-1) in numset:
                continue
            l = 1
            while((num+l) in numset):
                l += 1
            longest = max(longest,l)
        return longest