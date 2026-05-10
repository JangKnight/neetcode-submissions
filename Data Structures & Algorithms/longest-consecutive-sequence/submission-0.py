class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums_set = set(nums)

        for num in nums:
            streak, current = 0, num
            while current in nums_set: #check
                streak += 1
                current += 1
            longest = max(longest, streak)
        return longest