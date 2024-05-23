class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        current = []

        def backtrack(i=0):
            if sum(current) == target:
                combinations.append(current.copy())
                return

            if sum(current) > target or i == len(candidates):
                return

            # Include current element
            current.append(candidates[i])
            backtrack(i)

            # Do not include current element
            current.pop()
            backtrack(i + 1)

        backtrack()
        return combinations