class Solution:
    def reverseWords(self, s: str) -> str:
        reversedStr = ""

        stack = s.split()
        
        while stack != []:
            word = stack.pop()
            reversedStr += word + ' '

        return reversedStr[:-1]