#
# @lc app=leetcode.cn id=665 lang=python
#
# [665] 非递减数列
#
# https://leetcode-cn.com/problems/non-decreasing-array/description/
#
# algorithms
# Easy (19.55%)
# Likes:    150
# Dislikes: 0
# Total Accepted:    6K
# Total Submissions: 30K
# Testcase Example:  '[4,2,3]'
#
# 给定一个长度为 n 的整数数组，你的任务是判断在最多改变 1 个元素的情况下，该数组能否变成一个非递减数列。
#
# 我们是这样定义一个非递减数列的： 对于数组中所有的 i (1 <= i < n)，满足 array[i] <= array[i + 1]。
#
# 示例 1:
#
#
# 输入: [4,2,3]
# 输出: True
# 解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
#
#
# 示例 2:
#
#
# 输入: [4,2,1]
# 输出: False
# 解释: 你不能在只改变一个元素的情况下将其变为非递减数列。
#
#
# 说明:  n 的范围为 [1, 10,000]。
#
#
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
# class Solution {
#     public boolean checkPossibility(int[] nums) {
#         int length = nums.length;
#         int count = 0;
#         for (int i = 1; i < length && count < 2; i++) {
#             if (nums[i] >= nums[i - 1]) {
#                 continue;
#             }
#             count++;
#             if (i - 2 >= 0 && nums[i - 2] > nums[i]) {
#                 nums[i] = nums[i - 1];	 //使当前数字等于先前的数字
#             } else {
#                 nums[i - 1] = nums[i];	//使前一个数字小于或等于当前数字
#             }
#         }
#         return count <= 1;
#     }
# }

        length = len(nums)
        count = 0
        i = 1
        while i < length and count < 2:
            if nums[i-1] <= nums[i]:
                i += 1
                continue
            count += 1
            if (i-2>=0 and nums[i-2] > nums[i]):
                nums[i] = nums[i-1]
            else:
                nums[i-1] = nums[i]
            i += 1
        return count < 2


if __name__ == "__main__":
    s = Solution().checkPossibility([4,2,3])
    print(s)
    s = Solution().checkPossibility([3,4,2,3])
    print(s)

