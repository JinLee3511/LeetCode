class Solution:
    def intToRoman(self, num: int) -> str:
        numMap = {
            1: "I",
            4: "IV",
            5: "V",    
            9: "IX",
            10: "X",   
            40: "XL",
            50: "L",   
            90: "XC",
            100: "C",  
            400: "CD",
            500: "D",  
            900: "CM",
            1000: "M", 
        }

        res = ""

        for n in reversed(numMap.keys()):
            while n <= num:
                res += numMap[n]
                num -= n
        
        return res

s = Solution()
num = 3749
print(s.intToRoman(num))