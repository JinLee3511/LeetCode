class Solution {
    func search(_ nums: [Int], _ target: Int) -> Int {
        var i = 0
        var j = nums.count

        while (i <= j) {
            var mid = Int((i+j)/2)

            // Found Target
            if nums[mid] == target {
                return mid
            }

            // Could Not Find
            if j-i == 1 {
                break
            }

            // Go Left
            if nums[mid] > target {
                j = mid
            }
            // Go Right
            else {
                i = mid
            }
        }

        return -1
    }
}