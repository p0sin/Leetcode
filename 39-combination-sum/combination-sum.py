class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        cur = []

        def helper(i):
            if sum(cur) > target or i >= len(candidates):
                return
            if sum(cur) == target:
                ans.append(cur.copy())
                return
            
            # keep including candidates[i]
            cur.append(candidates[i])
            helper(i)

            # stop including candidates[i]
            cur.pop()
            helper(i + 1)

        helper(0)
        return ans