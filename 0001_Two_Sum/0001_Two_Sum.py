class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        targetValues: Store elem's index and value that adds up to the target as key
        - Key: (Target - elem) in nums
        - Value: index of the elem
        '''
        targetValues = {}

        # Save Values to add up to the Target
        for i, num in enumerate(nums):
            valueToAdd = target - num

            # Ignore Values already stored
            if valueToAdd in targetValues:
                continue

            targetValues[valueToAdd] = i

        # Find Answer
        for i, num in enumerate(nums):
            # Found Answer with unique element (not same index)
            if num in targetValues and i != targetValues[num]:
                return [i, targetValues[num]]
            
        # Not Found
        return [-1, -1]