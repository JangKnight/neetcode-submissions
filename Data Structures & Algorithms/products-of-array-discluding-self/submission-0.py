class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prod_arr = [0] * n

        for idx1, num1 in enumerate(nums):
            prod = 1
            for idx2, num2 in enumerate(nums):
                if idx1 == idx2:
                    continue
                prod *= num2
            
            prod_arr[idx1] = prod
        return prod_arr

        