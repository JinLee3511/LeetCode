function groupAnagrams(strs: string[]): string[][] {
    const groupedAnagrams= new Map<string, string[]>();

    // Read all elems from strs
    for (let elem of strs) {
        // Sort elem by chracter
        const sortedElem = [...elem].sort().join('');

        // Anagram Group Exists: append to new group
        if (groupedAnagrams.has(sortedElem)) {
            const anagrams: string[] = groupedAnagrams.get(sortedElem) ?? [];
            groupedAnagrams.set(sortedElem, [...anagrams, elem]);
        }
        // Anagram Group Does Not Exist
        else {
            groupedAnagrams.set(sortedElem, [elem]);
        }
    }

    return Array.from(groupedAnagrams, ([key, value]) => value);
};