class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        prefix_sum = 0
        highest = 0

        for g in gain:
            prefix_sum += g

            if prefix_sum > highest:
                highest = prefix_sum

        return highest