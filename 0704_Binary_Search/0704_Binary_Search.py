from typing import List

class Solution: 
    def search(self, nums: List[int], target: int) -> int:
        i = 0 # first index
        j = len(nums) # last index

        while i <= j:
            mid = (i+j)//2

            # Found Target
            if nums[mid] == target:
                return mid

            # Could Not Find
            if j-i == 1:
                break

            # Go Left
            if nums[mid] > target:
                j = mid
            
            # Go Right
            else:
                i = mid

        # Could not find
        return -1

s = Solution()
print(s.search([-1,0,3,5,9,12], 2))