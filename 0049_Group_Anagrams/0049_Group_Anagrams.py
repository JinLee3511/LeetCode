from typing import List
from collections import defaultdict 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groupedAnagrams = defaultdict(list) 
        
        # O(n^2logn)
        # Read Elements in strs
        for elem in strs: # O(n)
            # Sort Chracters in elem
            elemSorted = sorted(elem) # O(nlogn)
            # Create new string with sorted chracters of elem
            elemStr = "".join(elemSorted) # O(n)
            # Group them
            groupedAnagrams[elemStr].append(elem) # O(1)

        return groupedAnagrams.values()