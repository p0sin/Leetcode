class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = []
        cur = []

        def helper(i):
            if i >= len(nums):
                ans.append(cur.copy())
                return

            # include nums[i]
            cur.append(nums[i])
            helper(i + 1)

            # not include nums[i]
            cur.pop()
            helper(i + 1)

        helper(0)
        return ans

        