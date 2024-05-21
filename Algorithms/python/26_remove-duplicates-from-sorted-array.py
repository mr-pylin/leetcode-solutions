# https://leetcode.com/problems/remove-duplicates-from-sorted-array
# difficulty: easy

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        k = 1  # number of uniques [it can also act as the position]

        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        return k



if __name__ == '__main__':
    nums = [1, 1, 2]
    print(Solution().removeDuplicates(nums))