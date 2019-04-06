#
# @lc app=leetcode.cn id=461 lang=python
#
# [461] 汉明距离
#
# https://leetcode-cn.com/problems/hamming-distance/description/
#
# algorithms
# Easy (67.46%)
# Total Accepted:    15.9K
# Total Submissions: 23.2K
# Testcase Example:  '1\n4'
#
# 两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
#
# 给出两个整数 x 和 y，计算它们之间的汉明距离。
#
# 注意：
# 0 ≤ x, y < 2^31.
#
# 示例:
#
#
# 输入: x = 1, y = 4
#
# 输出: 2
#
# 解释:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
# ⁠      ↑   ↑
#
# 上面的箭头指出了对应二进制位不同的位置。
#
#
#
class Solution(object):
    bits = [2**i for i in range(32)]
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        ret = 0

        tmp = x ^ y
        for i in Solution.bits:
            if (tmp & i) == i:
                ret += 1
        return ret

if __name__ == "__main__":
    s = Solution().hammingDistance(1, 4)
    print(s)

