function search(nums: number[], target: number): number {
    var i = 0;
    var j = nums.length;

    while (i <= j) {
        var mid = Math.floor((i+j)/2);

        // Found Target
        if (nums[mid] === target) {
            return mid;
        }

        // Could Not Find
        if (j-i === 1) {
            break;
        }

        // Go Left
        if (nums[mid] > target) {
            j = mid;
        }

        // Go Right
        else {
            i = mid;
        }
    }

    // Could Not Find
    return -1;
};