class Solution {
    func buildArray(_ nums: [Int]) -> [Int] {
        var answerArr: [Int] = []
        
        for i in 0..<nums.count{
            answerArr.append(nums[nums[i]])
        }
        
        return answerArr
        
    }
}