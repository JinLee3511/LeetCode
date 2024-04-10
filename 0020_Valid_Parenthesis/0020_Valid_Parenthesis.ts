function isValid(s: string): boolean {
    var stack: string[] = [];
    const opp = new Map([
        [')', '('],
        ['}', '{'],
        [']', '[']
    ])

    for (let ch of s) {
        // Found Closing Parenthesis
        if (opp.has(ch)) {
            // Closing comes earlier than opening -> Invalid
            if (stack.length === 0) {
                return false;
            }
            
            const lastSeen = stack.pop();

            // Unmatching parenthesis -> Invalid
            if (lastSeen !== opp.get(ch)) {
                return false;
            }
        }

        // Opening Parenthesis
        else {
            stack.push(ch);
        }
    }

    return stack.length === 0;
};