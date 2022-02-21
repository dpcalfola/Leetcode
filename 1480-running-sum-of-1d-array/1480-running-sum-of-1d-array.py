class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer_list = []
        sum_of = 0
        for i in nums:
            sum_of += i
            answer_list.append(sum_of)

        return answer_list