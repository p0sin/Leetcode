class Solution:
    def rob(self, nums: List[int]) -> int:

        def memoization(nums, cache, index):
            if index == len(nums) - 2 or index == len(nums) - 1:
                return nums[index]
            if index in cache:
                return cache[index]
            if index >= len(nums) - 2:
                return 0

            cache[index] = nums[index] + max(memoization(nums, cache, index + 2), memoization(nums, cache, index + 3))

            return cache[index]

        return max(memoization(nums, {}, 0), memoization(nums, {}, 1))


