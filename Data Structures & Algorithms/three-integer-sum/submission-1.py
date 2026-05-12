class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        nums_map = defaultdict(int)

        for num in nums:
            nums_map[num] += 1
        
        three_num_arr = []
        for i in range(len(nums)):
            nums_map[nums[i]] -= 1
            if i and nums[i] == nums[i-1]: 
                continue

            for j in range(i+1, len(nums)):
                nums_map[nums[j]] -= 1

                if j-1 > i and nums[j] == nums[j-1]:
                    continue
                
                diff_to_zero = (nums[i] + nums[j]) * -1

                if nums_map[diff_to_zero]:
                    three_num_arr.append([nums[i], nums[j], diff_to_zero])
            for j in range(i+1, len(nums)):
                nums_map[nums[j]] += 1

        return three_num_arr