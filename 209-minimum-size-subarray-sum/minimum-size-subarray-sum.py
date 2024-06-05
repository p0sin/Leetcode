class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L, total, res = 0, 0, float("inf")

        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                res = min(res, (R - L + 1))
                total -= nums[L]
                L += 1

        return 0 if res == float("inf") else res