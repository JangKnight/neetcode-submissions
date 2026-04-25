class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        print(nums)
        for idx, _ in enumerate(nums):
            if idx > 0:
                if nums[idx - 1] == nums[idx]:
                    return True
        return False

        
                
        