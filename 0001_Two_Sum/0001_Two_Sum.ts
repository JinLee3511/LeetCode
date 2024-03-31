function twoSum(nums: number[], target: number): number[] {
    /**
     * targetValues: Store elem's index and value that adds up to the target as key
     * - Key: (Target - elem) in nums
     * - Value: index of the elem
     */
    const targetValues = new Map();

    // Find Matches while storing index and the value
    for (let i=0; i<nums.length; i++) {

        // Found Target
        if (targetValues.has(target - nums[i])) {
            return [i, targetValues.get(target - nums[i])]; 
        }
        
        // Not Found, save the index and the value
        targetValues.set(nums[i], i);
    }

    // Not Found At All
    return [-1, -1];
};

const numsInput: number[] = [2,7,11,15];
const targetInput: number = 9;

console.log(twoSum(numsInput, targetInput));