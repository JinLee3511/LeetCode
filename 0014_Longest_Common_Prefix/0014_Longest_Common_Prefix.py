from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for word in strs:
            new_prefix = ""
            for ch_i, ch_j in zip(word, prefix):
                if ch_i == ch_j:
                    new_prefix += ch_i
                else:
                    break
            
            prefix = new_prefix
            
        return prefix