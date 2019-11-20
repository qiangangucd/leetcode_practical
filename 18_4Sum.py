'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''


class Solution(object):
    ELEMENTS = 4  # parametrise the number of elements being summed

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        self.n_sum(sorted(nums), target, [], self.ELEMENTS, results)
        return results

    def n_sum(self, nums, target, partial, n, results):
        if len(nums) < n or target > nums[-1] * n or target < nums[0] * n:
            return
        if n == 2:
            left = 0
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    results.append(partial + [nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[right] == nums[right + 1] and left < right:
                        right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        else:
            for i in range(len(nums) - n + 1):
                if i == 0 or nums[i] != nums[i - 1]:
                    self.n_sum(nums[i + 1:], target - nums[i], partial + [nums[i]], n - 1, results)


if __name__ == '__main__':
    ans = Solution()
    print(ans.fourSum([-3, -2, -1, 0, 0, 1, 2, 3], 0))
