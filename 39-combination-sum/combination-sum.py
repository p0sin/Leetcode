class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def helper(i, cur, total):
            if total == target:
                ans.append(cur.copy())
                return
            if total > target or i >= len(candidates):
                return

            
            # keep including candidates[i]
            cur.append(candidates[i])
            helper(i, cur, total + candidates[i])

            # stop including candidates[i]
            cur.pop()
            helper(i + 1, cur, total)

        helper(0, [], 0)
        return ans