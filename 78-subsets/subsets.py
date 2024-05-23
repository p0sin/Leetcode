class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        current = []

        def backtrack(i=0):
            if i == len(nums):
                subsets.append(current.copy())  # Append a copy to avoid modifications
                return

            # Include the current element
            current.append(nums[i])
            backtrack(i + 1)  # Explore with the current element included

            # Exclude the current element (backtrack)
            current.pop()
            backtrack(i + 1)  # Explore without the current element included

        backtrack()
        return subsets
