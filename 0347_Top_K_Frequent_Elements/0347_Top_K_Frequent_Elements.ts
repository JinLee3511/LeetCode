// Time Complexity: O(n)
function topKFrequent(nums: number[], k: number): number[] {
    // @ts-ignore
    // @ts-nocheck
    // @ts-check
    const numCount = new Map<number, number>();

    // Count Numbers
    for (let num of nums) {
        numCount.set(num, (numCount.get(num) || 0) + 1);
    }

    // Create size of nums array of arrays
    // @ts-ignore
    // @ts-nocheck
    // @ts-check
    const sortedNum: number[][] = Array.from({length: nums.length + 1}, () => []);
    
    // Store num in the appropriate index (count)
    // @ts-ignore
    // @ts-nocheck
    // @ts-check
    for (const [num, count] of Array.from(numCount.entries())) {
        sortedNum[count].push(num);
    }

    // Get Answer
    var res: number[] = []
    for (let i=sortedNum.length - 1; i > -1; i--) {

        // Nothing in the i count; skip
        if (sortedNum[i].length === 0) {
            continue;
        }
        // O(k) where sum(k_i) == n
        for (let num of sortedNum[i]) {
            res.push(num);
            if (res.length === k) {
                return res;
            }
        }
    }

    return res;
}
