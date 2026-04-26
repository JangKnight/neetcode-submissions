class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 1
            else: 
                nums_dict[num] += 1
        
        freq_arr = []
        for num, freq in nums_dict.items():
            freq_arr.append([freq, num])
        freq_arr.sort()

        res = []
        while len(res) < k:
            res.append(freq_arr.pop()[1])
        
        return res

        