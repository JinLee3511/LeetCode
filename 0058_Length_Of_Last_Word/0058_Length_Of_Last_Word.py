class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split()
        return len(arr[-1])


s = Solution()
string = "   fly me   to   the moon  "
print(s.lengthOfLastWord(string))