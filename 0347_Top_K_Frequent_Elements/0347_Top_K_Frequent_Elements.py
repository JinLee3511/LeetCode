from typing import List

from heapq import heapify, heappop, heappush

class Solution:
    # O(nlog(k+1)) using minHeap
    def topKFrequentHeap(self, nums: List[int], k: int) -> List[int]:
        # Count nums 
        # (num, frequency)
        # Time: O(n), Space: O(n)
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] = freq[num] + 1
            else:
                freq[num] = 1

        # Use MaxHeap to save top k most frequent nums
        # Time: O(nlog(k+1)), Space: O(n) where k+1 <= n
        minHeap = []
        heapify(minHeap)
        heapSize = 0

        for num in freq.keys(): # O(n)
            # O(log(k+1))
            heappush(minHeap, (freq[num], num)) # pushed by the first pair value (frequency)
            heapSize = heapSize + 1

            # Exceeds more than K, remove the smallest frequency
            if heapSize > k:
                heappop(minHeap) # O(1)
                heapSize = heapSize - 1
            
        return [num for freq, num in minHeap]

    # O(n) using bucket sort approach
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Count num
        # O(n)
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Index as counts, elements are stored as [] where each item in arr is the number
        sortedNum = [[] for i in range(len(nums)+1)]

        # Initialize sortedNum
        for num, count in freq.items():
            sortedNum[count].append(num)

        res = []

        # Find Top K frequent
        # O(n)
        for i in range(len(sortedNum)-1, 0, -1):
            # O(1) if array empty
            # O(k) s.t sum(k_i) = n
            for num in sortedNum[i]:
                res.append(num)
                if len(res) == k:
                    return res