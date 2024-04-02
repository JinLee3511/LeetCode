class Solution {
    func isAnagram(_ s: String, _ t: String) -> Bool {

        // Base Cases
        // Length Different -> Not Anagram
        if s.count != t.count {
            return false
        }
        // Both Lenght of 0 -> Anagram
        if (s.count == 0 && t.count == 0) {
            return true
        }

        var sCnt: [Character: Int] = [:]

        // Count characters of s
        for ch: Character in s {
            // Increment Character
            if let cnt: Int = sCnt[ch] {
                sCnt[ch] = 1 + cnt
            }
            // character first seen
            else {
                sCnt[ch] = 1
            }
        }

        // Decrement character by one if a character exists in s exists in t
        for ch: Character in t {
            // Increment Character
            if let cnt: Int = sCnt[ch] {
                // Found more ch in t than s
                if cnt == 0 {
                    return false
                }
                sCnt[ch] = cnt - 1
            }
            // character found in t is not in s
            else {
                return false
            }
        }
        
        // Compare Counts of Characters
        for (ch, cnt) in sCnt {
            // Character found in s has more ch's than t
            if cnt > 0 {
                return false
            }
        }
        
        // All Character Count Match -> Anagram
        return true
    }
}