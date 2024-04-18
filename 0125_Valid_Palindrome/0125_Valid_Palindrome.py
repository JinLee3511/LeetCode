import re

class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned = ""

        # Remove white spaces and leave only alphabets
        for ch in s:
            if not ch.isalnum():
                continue
            
            cleaned += ch.lower()

        i = 0
        j = len(cleaned)-1

        while i <= j:
            if cleaned[i] != cleaned[j]:
                return False

            i += 1
            j -= 1

        return True
            
            


s = Solution()
inp = "10P01"
print(s.isPalindrome(inp))