class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        hashMap = {}

        for a in arr:
            if a not in hashMap:
                hashMap[a] = 1
            else:
                hashMap[a] += 1

        duplicates = set()

        occurences = hashMap.values()

        for o in occurences:
            if o in duplicates:
                return False
            else:
                duplicates.add(o)

        return True

        