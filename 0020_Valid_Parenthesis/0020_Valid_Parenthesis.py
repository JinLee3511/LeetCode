class Solution:
    # Time O(n)
    # Space O(n)
    def isValid(self, s: str) -> bool:
        stack = []
        opp = {')' : '(', '}': '{', ']' : '['}
        
        # Odd Length -> Cannot be valid parenthesis
        if len(s) % 2 == 1:
            return False

        for elem in s:
            # Found closing
            if elem in opp:
                # Closing parenthesis was found ealier than opening
                if len(stack) == 0:
                    return False

                # get last seen opening from stack
                lastSeen = stack.pop()
                
                # Found Unmatching parenthesis
                if lastSeen != opp[elem]:
                    return False

            # Save opening parenthesis into stack
            else:
                stack.append(elem)
            
        # Everything matched (stack empty) -> Valid Parenthesis
        return len(stack) == 0