class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # MERGE SORT
        def mergesort(nums):
            # Base Case
            if len(nums) <= 1:
                return nums

            midIndex = len(nums) // 2
            leftArr = mergesort(nums[:midIndex])
            rightArr = mergesort(nums[midIndex:])

            return merge(leftArr, rightArr)

        def merge(left, right):
            output = []
            l, r = 0, 0

            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    output.append(left[l])
                    l += 1
                else:
                    output.append(right[r])
                    r += 1
            
            if l == len(left):
                output += right[r:]
            else:
                output += left[l:]

            return output

        return mergesort(nums)




        