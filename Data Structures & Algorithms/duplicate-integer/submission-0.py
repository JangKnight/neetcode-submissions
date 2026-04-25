class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for idx1, num1 in enumerate(nums):
            for idx2, num2 in enumerate(nums):
                if idx1 == idx2:
                    continue
                if num1 == num2:
                    return True
        return False
                
        