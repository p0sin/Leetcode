class Solution():
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        complements = {}

        for i in range(len(nums)):
            number = nums[i]
            complement = target - nums[i] 
            if complement in complements:
                answer = [i, complements[complement]]
                return answer
            else:
                complements[number] = i

solution = Solution()
array = [3,2,4]
target = 6
print(solution.twoSum(array, target))

