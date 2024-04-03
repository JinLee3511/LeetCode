class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Length Not Equal -> Not Anagram
        if len(s) != len(t): 
            return False

        # Both length 0 -> Anagram
        if len(s) == 0 and len(t) == 0:
            return True

        sCnt = {}

        # Count characters in s
        for ch in s:
            if ch in sCnt:
                sCnt[ch] = sCnt[ch] + 1
            else:
                sCnt[ch] = 1

        # Decrement counts of ch if both in s and t
        for ch in t:
            # ch both in s and t
            if ch in sCnt:
                # t has more ch's than s -> Not Anagram
                if sCnt[ch] == 0:
                    return False
                # Decrement count
                else:
                    sCnt[ch] = sCnt[ch] - 1

            # ch in t is not in s -> Not Anagram
            else:
                return False

        for ch in sCnt:
            # s has more ch's than t -> Not Anagram
            if sCnt[ch] > 0:
                return False
        
        # All ch counts match
        return True