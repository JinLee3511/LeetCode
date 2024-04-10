class Solution {
    func topKFrequent(_ nums: [Int], _ k: Int) -> [Int] {
        var numCount: [Int: Int] = [:]

        // Count num
        for num: Int in nums {
            if let cnt: Int = numCount[num]{
                numCount[num] = 1 + cnt
            }
            else {
                numCount[num] = 1
            }
        }

        var sortedNum: [[Int]] = Array(repeating: [Int](), count: nums.count + 1)

        // Save into right count (index)
        for (num, cnt) in numCount {
            sortedNum[cnt].append(num)
        }

        // Return Result
        var res: [Int] = []
        for i in stride(from: sortedNum.count-1, to: -1, by: -1) {
            if sortedNum[i].isEmpty {
                continue
            }

            for num in sortedNum[i] {
                res.append(num)

                if res.count == k {
                    return res
                }
            }
        }

        return res
    }   
}