class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        index = 0

        for i in range(len(nums)):
            # if 
            if nums[i] != 0:
                if nums[index] != 0:
                    index += 1
                else:
                    temp = nums[index]
                    nums[index] = nums[i]
                    nums[i] = temp
                    index += 1
        