class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        half_size = len(nums) / 2
        nums_set = set(nums)
        print(nums_set)

        for i in nums_set:
            if nums.count(i) > half_size:
                return i

        return -1
        