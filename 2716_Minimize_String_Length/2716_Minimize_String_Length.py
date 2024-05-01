class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))


string = "aaabbc"
s = Solution()
print(s.minimizedStringLength(string))