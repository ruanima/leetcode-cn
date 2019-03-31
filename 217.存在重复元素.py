#
# @lc app=leetcode.cn id=217 lang=python
#
# [217] 存在重复元素
#
# https://leetcode-cn.com/problems/contains-duplicate/description/
#
# algorithms
# Easy (46.04%)
# Total Accepted:    48.8K
# Total Submissions: 102.6K
# Testcase Example:  '[1,2,3,1]'
#
# 给定一个整数数组，判断是否存在重复元素。
#
# 如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。
#
# 示例 1:
#
# 输入: [1,2,3,1]
# 输出: true
#
# 示例 2:
#
# 输入: [1,2,3,4]
# 输出: false
#
# 示例 3:
#
# 输入: [1,1,1,3,3,4,3,2,4,2]
# 输出: true
#
#

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # if len(set(nums)) != len(nums):
        #     return True
        # return False

        nums_set = set()
        count = 0
        for i in nums:
            nums_set.add(i)
            count += 1
            if len(nums_set) != count:
                return True
        return False
