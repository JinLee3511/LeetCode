function containsDuplicate(nums: number[]): boolean {
    const numbers = new Set<number>();

    for (let i=0; i<nums.length; i++) {
        // Found Duplicate
        if (numbers.has(nums[i])) {
            return true;
        }
        numbers.add(nums[i]);
    }
    return false;
};