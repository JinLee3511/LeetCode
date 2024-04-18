from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, num in enumerate(nums):
            # Skip Same nums on the left (remove duplicate)
            if i > 0 and num == nums[i-1]:
                continue

            l = i+1
            r = len(nums)-1

            # Find 3 Sum that adds up to the target
            # This will skip cases where index out of range
            while l < r:
                threeSum =  nums[l] + nums[r] + num

                # Found 3 Sum
                if threeSum == 0:
                    res.append([num, nums[l], nums[r]])
                    r -= 1

                    # Skip Same nums on the right (remove duplicate)
                    while l < r and nums[r+1] == nums[r]:
                        r -= 1

                # Make Sum larger (move left pointer to right)
                elif threeSum < 0:
                    l += 1
                
                # Make Sum smaller (move right pointer to left)
                else:
                    r -= 1

        return res

s = Solution()
arr = [-2,0,1,1,2]
print(sorted(arr))
print(s.threeSum(arr))