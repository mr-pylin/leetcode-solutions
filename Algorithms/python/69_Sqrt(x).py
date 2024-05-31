# https://leetcode.com/problems/sqrtx
# difficulty: easy

from typing import List


class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        threshold = x // 2
        while True:
            if threshold ** 2 > x:
                threshold //= 2
            elif threshold ** 2 <= x:
                while (threshold + 1) ** 2 <= x:
                    threshold += 1
                else:
                    break

        return threshold


if __name__ == '__main__':
    x = 8
    print(Solution().mySqrt(x))
