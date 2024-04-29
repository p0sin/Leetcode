class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = maxCons = 0

        for r, num in enumerate(nums):
            k -= 1 - num

            if k < 0:
                k += 1 - nums[l]

                l += 1
            else:
                maxCons = max(maxCons, r - l + 1)

        return maxCons