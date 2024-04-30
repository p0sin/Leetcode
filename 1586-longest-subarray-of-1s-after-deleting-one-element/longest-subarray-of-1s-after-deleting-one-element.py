class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, 0
        n = len(nums)
        zeros = 0
        maxLength = 0

        while r < n:
            if nums[r] == 0:
                zeros += 1
            while l < n and zeros == 2:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            maxLength = max(r - l, maxLength)
            r += 1
        return maxLength



            
             
        