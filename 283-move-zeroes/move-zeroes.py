class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pointer = None

        for i in range(len(nums)):
            if nums[i] == 0:
                pointer = i
                break

        if pointer == None:
            return
            
        for i in range(pointer, len(nums)):  
            if nums[i] != 0:
                nums[pointer] = nums[i]
                nums[i] = 0
                pointer += 1

