class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsSet = set(nums)

        for n in nums:
            if n in numsSet:
                numsSet.remove(n)
            else:
                return True
        return False

        
        