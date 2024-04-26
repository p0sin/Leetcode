class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height) - 1
        switch, max = 0, 0

        while i < j:
            b = j - i
            h = min(height[i], height[j])
            rec = b * h

            if rec > max:
                max = rec
            
            if height[j] > height[i]:
                i += 1
            else:
                j -= 1

        return max

        