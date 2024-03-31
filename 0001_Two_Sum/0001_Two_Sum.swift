class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var targetValues:[Int: Int] = [:]

        for i: Int in 0...nums.count-1 {
            // Found Match
            if let savedValueToAddIndex: Int = targetValues[target - nums[i]] {
                return [i, savedValueToAddIndex]
            }
            // Save index and value
            targetValues[nums[i]] = i
        }

        return [-1, -1]
    }
}