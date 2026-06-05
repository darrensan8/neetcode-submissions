class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set(nums)
        seen2=list(seen)
        if sorted(seen2) == sorted(nums):
            return False
        else:
            return True