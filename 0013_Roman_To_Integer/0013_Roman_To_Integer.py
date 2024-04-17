class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        prevCh = ''
        count = 0

        for i, ch in enumerate(s):

            if prevCh != '':
                # Smaller value comes earlier than larger value -> subtract
                if d[prevCh] < d[ch]:
                    count -= d[prevCh]

                # Normal Flow -> add previous and current value
                else:
                    count += d[prevCh]

            # Add Last One
            if len(s)-1 == i:
                count += d[ch]

            prevCh = ch

        return count