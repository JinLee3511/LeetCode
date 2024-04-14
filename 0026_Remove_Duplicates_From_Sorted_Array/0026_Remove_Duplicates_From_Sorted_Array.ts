function removeDuplicates(nums: number[]): number {
    var i = 0;

    for (let j = 1; j<nums.length; j++) {
        // Element not equal, then save it to the right position
        if (nums[i] !== nums[j]) {
            i = i + 1;
            nums[i] = nums[j];
        }
    }

    return i + 1;
}