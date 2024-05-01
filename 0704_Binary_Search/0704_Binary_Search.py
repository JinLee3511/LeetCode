from typing import List

class Solution: 
    def search(self, nums: List[int], target: int) -> int:
        i = 0 # first index
        j = len(nums)-1 # last index

        while i <= j:
            mid = (i+j)//2

            # Found Target
            if nums[mid] == target:
                return mid

            # Go Left
            if nums[mid] > target:
                j = mid-1
            
            # Go Right
            else:
                i = mid+1

        # Could not find
        return -1