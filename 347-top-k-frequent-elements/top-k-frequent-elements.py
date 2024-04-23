class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Create a Hash Map for each number as key and n seen as values
        reps = {}

        for number in nums:
            if number in reps:
                reps[number] += 1
            else:
                reps[number] = 1

        # Create buckets for n elements
        buckets = [[] for i in range(len(nums) + 1)]
        
        # Sort dict to get an order list of most frequent elements
        for key, value in reps.items():
            buckets[value].append(key)

        output = []
        for i in range(len(buckets) - 1, 0, -1):
            for j in buckets[i]:
                output.append(j)
                if len(output) == k:
                    return output
            





        