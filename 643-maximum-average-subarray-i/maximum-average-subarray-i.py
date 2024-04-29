class Solution(object):
    def findMaxAverage(self, nums, k):
        if len(nums) == 1:
            return float(nums[0])
        
        start = 0
        end = k
        average = 0.0
        
        # Calculate the average of the first window
        for i in range(k):
            average += float(nums[i]) / k
        
        # Initialize the maximum average
        max_average = average
        
        # Slide the window and update the maximum average
        while end < len(nums):
            average = average - float(nums[start]) / k
            average = average + float(nums[end]) / k
            max_average = max(max_average, average)
            start += 1
            end += 1
        
        return max_average
