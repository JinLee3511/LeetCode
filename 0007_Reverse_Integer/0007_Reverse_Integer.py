class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            negative = True

        s = str(x)
        
        if negative:
            s = s[1:]

        s = s[::-1]
        s = int(s)

        if negative:
            s *= -1

        if s <= 2**31 - 1 and s >= -2**31:
            return s
        else:
            return 0