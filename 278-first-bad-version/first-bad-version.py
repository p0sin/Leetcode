# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n

        while l <= r:
            mid = (l + r) // 2
            if isBadVersion(mid) is False:
                l = mid + 1
            elif isBadVersion(mid) and isBadVersion(mid - 1):
                r = mid - 1
            else:
                return mid

            
        