function isAnagram(s: string, t: string): boolean {
    // Length not equal -> Not Anagram
    if (s.length !== t.length) {
        return false;
    }
    // Length Both 0 -> Anagram
    if (s.length === 0 && t.length === 0) {
        return true;
    }

    const sCnt = new Map<string, number>();

    // Count characters in s
    for (let ch of s) {
        // Found more ch's
        if (sCnt.has(ch)) {
            let curCnt = sCnt.get(ch) ?? 0;
            sCnt.set(ch, 1 + curCnt);
        }
        // Initialize first ch
        else {
            sCnt.set(ch, 1);
        }
    }

    // Count characters in t
    for (let ch of t) {
        // Found ch in t and s
        if (sCnt.has(ch)) {
            // t has more ch than s -> Not Anagram
            let curCnt = sCnt.get(ch) ?? -1; // error handling later
            if (curCnt === 0) {
                return false;
            }
            sCnt.set(ch, curCnt - 1);
        }
        // Unique ch in t but not in s -> Not Anagram
        else {
            return false;
        }
    }

    // All Characters Match
    return true;
}