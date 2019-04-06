#
# @lc app=leetcode.cn id=976 lang=python
#
# [976] 最小面积矩形
#
# https://leetcode-cn.com/problems/largest-perimeter-triangle/description/
#
# algorithms
# Easy (58.15%)
# Total Accepted:    3K
# Total Submissions: 5.3K
# Testcase Example:  '[2,1,2]'
#
# 给定由一些正数（代表长度）组成的数组 A，返回由其中三个长度组成的、面积不为零的三角形的最大周长。
#
# 如果不能形成任何面积不为零的三角形，返回 0。
#
#
#
#
#
#
# 示例 1：
#
# 输入：[2,1,2]
# 输出：5
#
#
# 示例 2：
#
# 输入：[1,2,1]
# 输出：0
#
#
# 示例 3：
#
# 输入：[3,2,3,4]
# 输出：10
#
#
# 示例 4：
#
# 输入：[3,6,2,3]
# 输出：8
#
#
#
#
# 提示：
#
#
# 3 <= A.length <= 10000
# 1 <= A[i] <= 10^6
#
#
#
class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return

        A.sort(reverse=True)
        # print(A)
        for i in range(len(A)-2):
            # print(A[i], A[i+1], A[i+2])
            if (A[i] - A[i+2] < A[i+1] ) and (A[i+1] + A[i+2] > A[i]):
                return A[i] + A[i+2] + A[i+1]
        return 0

if __name__ == "__main__":
    t = Solution().largestPerimeter([3,6,2,3])
    print(t)
