class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Create a dict to save number already seen
        previous_dict = {}
        # Iterate through loop
        for current in nums:
            # Check if current is in previous_dict
            if current in previous_dict:
                return True
            else:
                previous_dict[current] = True
        return False