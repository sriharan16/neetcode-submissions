class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        res = []
        nums.sort()

        for i in range(len(nums)-2):
            a = nums[i]

            if a > target:
                break
            
            if i > 0 and nums[i-1] == a:
                continue
            
            l,r = i+1, len(nums)-1

            while l<r:
                ts = a + nums[l] + nums[r]

                if ts == target:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -=1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
                elif ts < target:
                    l += 1
                else:
                    r -= 1
        return res

