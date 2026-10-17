class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,2,4,6]

        # [1, 1, 2, 8]
        # [48, 24, 6, 1]

        prefix, suffix, prefix_list, suffix_list = 1, 1, [], []

        for i in nums:
            prefix_list.append(prefix)
            prefix *= i
        
        for i in range(len(nums)):
            suffix_list.append(suffix)
            suffix *= nums[-i - 1]
        suffix_list.reverse()
        return [prefix_list[i] * suffix_list[i] for i in range(len(nums))]






