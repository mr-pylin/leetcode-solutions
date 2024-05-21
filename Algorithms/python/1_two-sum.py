# https://leetcode.com/problems/two-sum
# difficulty: easy

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # stop recalculating the array length in each for-loop
        n = len(nums)

        # exclude the last index in the first loop; it is handled in the second loop
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums, target))