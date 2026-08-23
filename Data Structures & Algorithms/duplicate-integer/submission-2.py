class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen: dict = defaultdict(int)
        for num in nums:
            seen[num] += 1

        if any(num > 1 for num in seen.values()):
            return True
        
        return False