class Solution {
    func containsDuplicate(_ nums: [Int]) -> Bool {
        var numbers: Set<Int> = []

        for num: Int in nums {
            // Found Duplicate
            if numbers.contains(num) {
                return true
            }
            numbers.insert(num)
        }
        return false
    }
}