class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        answer = []
        limit = len(nums) / 3
        set_nums = set(nums)

        for i in set_nums:
            if nums.count(i) > limit:
                answer.append(i)

        return answer