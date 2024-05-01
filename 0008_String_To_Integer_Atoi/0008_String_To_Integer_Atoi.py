class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.split()

        if len(s) == 0:
            return 0

        elem = s[0]
        i = 0
        num = 0
        sign = 1

        # Set sign
        if elem[0] == '+' or elem[0] == '-':
            sign = 1 if elem[0] == '+' else -1
            i += 1

        # Convert to Integer
        while i < len(elem) and elem[i].isdigit():
            num = num * 10 + int(elem[i])
            i += 1

        res = sign * num

        # Check Range
        if res > 2**31-1:
            return 2**31-1
        elif res < -2**31:
            return -2**31

        return res

s = Solution()
string = "  -91283472332   +-12"
print(s.myAtoi(string))