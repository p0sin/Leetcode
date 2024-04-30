class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        set1 = set(nums1)
        set2 = set(nums2)

        list1 = []
        list2 = []
        for n in set1:
            if n not in set2:
                list1.append(n)

        for n in set2:
            if n not in set1:
                list2.append(n)

        answer = [list1, list2]
        return answer
        