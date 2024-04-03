class Solution {
    func groupAnagrams(_ strs: [String]) -> [[String]] {
        var groupedAnagrams: [String: [String]] = [:]

        // Read str from strs
        for elem: String in strs {
            // Convert to sorted string
            let elemStr:String = String(elem.sorted())
            
            // Anagram group exists, append to existing group
            if groupedAnagrams.keys.contains(elemStr) {
                if var anagrams: [String] = groupedAnagrams[elemStr] {
                    anagrams.append(elem)
                    groupedAnagrams[elemStr] = anagrams
                }
            }
            // Anagram Group Does not exits, start a new group
            else {
                groupedAnagrams[elemStr] = [elem]
            }
        }

        return Array(groupedAnagrams.values)
    }
}