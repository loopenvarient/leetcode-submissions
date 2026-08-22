class Solution:
    def isValid(self, s: str) -> bool:

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []

        for ch in s:

            # Opening bracket
            if ch in "([{":
                stack.append(ch)

            # Closing bracket
            else:
                # No opening bracket to match
                if not stack:
                    return False

                top = stack.pop()

                # Check if brackets match
                if top != pairs[ch]:
                    return False

        # Stack should be empty if all brackets matched
        return len(stack) == 0