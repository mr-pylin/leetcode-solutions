# https://leetcode.com/problems/valid-parentheses
# difficulty: easy

class Solution:
    def isValid(self, s: str) -> bool:

        # odd length is not valid
        if len(s) % 2:
            return False
        
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
        
        # stack: last in first out [LIFO]
        stack = []

        for char in s:
            if char in pairs.keys():
                stack.append(char)  # save openings in the stack
            elif char in pairs.values():
                if len(stack) == 0 or char != pairs[stack.pop()]:  # pop the last item in the stack when reaching a closing character
                    return False
                
        if len(stack) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    s = "(){[]}"
    print(Solution().isValid(s))