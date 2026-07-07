class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = -1
        l = 0
        r = len(heights)-1
        while(l<r):
            a = min(heights[l], heights[r]) * (r-l)
            if (a > max_area):
                max_area = a
            if heights[l] <= heights[r]:
                l += 1
            else :
                r -= 1
        return max_area