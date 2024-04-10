class Solution {
    func isValid(_ s: String) -> Bool {
        var stack: [Character] = []
        let opp: [Character: Character] = ["]":"[", "}":"{", ")":"("]

        for ch: Character in s {
            // Found Closing
            if let oppCh: Character = opp[ch] {
                guard let lastSeen = stack.popLast() else { 
                    // closing came first than opening -> Invalid
                    return false 
                }

                // Unmatch -> Invalid
                if lastSeen != opp[ch] {
                    return false
                }
            }

            // Found Opening
            else {
                stack.append(ch)
            }
        }

        return stack.count == 0
    }
}