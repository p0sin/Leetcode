class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1

        res = (r - l) * min(height[l], height[r])

        while l < r:
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1

            res = max(res, (r - l) * min(height[l], height[r]))

        return res
        