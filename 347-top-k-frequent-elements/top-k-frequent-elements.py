class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Create a Hash Map for each number as key and n seen as values
        reps = {}

        for n in nums:
            reps[n] = 1 + reps.get(n, 0)

        # Create buckets for n elements
        buckets = [[] for i in range(len(nums) + 1)]
        
        # Allocate each frequency to its bucket
        for key, value in reps.items():
            buckets[value].append(key)

        # Loop through the buckets and retreieve top frequencies
        output = []
        for i in range(len(buckets) - 1, 0, -1):
            for j in buckets[i]:
                output.append(j)
                if len(output) == k:
                    return output
            





        