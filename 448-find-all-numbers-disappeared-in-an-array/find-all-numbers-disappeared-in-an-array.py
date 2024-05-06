class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        res = set()
        for i in range(1, len(nums) + 1):
            res.add(i)
            

        for n in nums:
            if n in res:
                res.remove(n)

        return list(res)
        