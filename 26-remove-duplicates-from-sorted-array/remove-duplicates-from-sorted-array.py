class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """ APROACH
        - Create a pointer at index 0 and iterate through the array
        - If n is a unique number, keep it and move pointer to next index
        - If it is not unique, hold the pointer at place until a unique value
        - Return the length of the unique values
        """

        prev = nums[0]
        p = 1
        ans = 1
        
        for i in range(1, len(nums)):
            if nums[i] > prev:
                nums[p] = nums[i]
                ans += 1
                prev = nums[i]
                p += 1

        return ans


