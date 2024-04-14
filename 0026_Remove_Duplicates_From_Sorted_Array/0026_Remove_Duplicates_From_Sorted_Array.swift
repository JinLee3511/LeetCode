class Solution {
    func removeDuplicates(_ nums: inout [Int]) -> Int {
        var i = 0;

        for j in 1..<nums.count {
            if nums[i] != nums[j] {
                i = i + 1
                nums[i] = nums[j]
            }
        }

        return i + 1
    }
}