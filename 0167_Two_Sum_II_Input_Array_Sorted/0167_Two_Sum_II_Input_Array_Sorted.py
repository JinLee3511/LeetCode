from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        i = 0
        j = len(numbers) - 1

        while i < j:
            # Found
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            
            # Move right pointer to left
            elif numbers[i] + numbers[j] > target:
                j -= 1
            
            else:
                i += 1

s = Solution()
arr = [2,7,11,15]
print(s.twoSum(arr, 9))