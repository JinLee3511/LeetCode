class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        targetValues: Store elem's index and value that adds up to the target as key
        - Key: (Target - elem) in nums
        - Value: index of the elem
        '''
        targetValues = {}

        for i in range(len(nums)):
            # Found Match
            if nums[i] in targetValues:
                return [targetValues[nums[i]], i]
            
            # Save Value and Index
            targetValues.update({target - nums[i]: i})
            
        # Not Found
        return [-1, -1]