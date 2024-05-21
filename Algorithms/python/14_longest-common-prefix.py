# https://leetcode.com/problems/longest-common-prefix
# difficulty: easy

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        maximum_prefix = min(map(len, strs)) # maximum prefix = minimum length

        # check for atmost <maximum_prefix> characters
        prefix = []
        for i in range(maximum_prefix):
            flag = True
            char = strs[0][i]

            for j in range(1, len(strs)):
                if strs[j][i] != char:
                    flag = False
                    break
            
            if flag:
                prefix.append(char)
            else:
                break

        return ''.join(prefix)


if __name__ == '__main__':
    strs = ['flower', 'flow', 'flight']
    print(Solution().longestCommonPrefix(strs))