class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        buckets = [0] * 3
        
        for b in nums:
            buckets[b] += 1

        i = 0

        for b in range(len(buckets)):
            for n in range(buckets[b]):
                nums[i] = b
                i += 1