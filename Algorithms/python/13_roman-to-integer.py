# https://leetcode.com/problems/roman-to-integer
# difficulty: easy

class Solution:
    def romanToInt(self, s: str) -> int:
        table = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        number = 0
        i = 0
        while i < len(s) - 1:
            if table[s[i]] < table[s[i + 1]]:
                number += table[s[i + 1]] - table[s[i]]
                i += 2
            else:
                number += table[s[i]]
                i += 1
        
        # if the above loop ended in <else> block, we shal include the last character which was ignored in the while condition
        if i == len(s) - 1:
            number += table[s[i]]

        return number


if __name__ == '__main__':
    s = 'MCMXCIV'
    print(Solution().romanToInt(s))