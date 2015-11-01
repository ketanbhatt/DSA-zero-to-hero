__author__ = 'ketanbhatt'

# Given an array of integers, find two numbers such that they add up to a specific target number.
#
# The function twoSum should return indices of the two numbers such that they add up to the target, where
# index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
#
# You may assume that each input would have exactly one solution.
#
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in xrange(len(nums)):
            for j in xrange(1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i+1, j+1]


nums = [1,2,3,4]
target = 5
print Solution().twoSum(nums, target)
