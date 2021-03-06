#
# @lc app=leetcode.cn id=605 lang=python
#
# [605] 种花问题
#
# https://leetcode-cn.com/problems/can-place-flowers/description/
#
# algorithms
# Easy (27.98%)
# Likes:    66
# Dislikes: 0
# Total Accepted:    7K
# Total Submissions: 24.4K
# Testcase Example:  '[1,0,0,0,1]\n1'
#
# 假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
#
# 给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数 n 。能否在不打破种植规则的情况下种入 n
# 朵花？能则返回True，不能则返回False。
#
# 示例 1:
#
#
# 输入: flowerbed = [1,0,0,0,1], n = 1
# 输出: True
#
#
# 示例 2:
#
#
# 输入: flowerbed = [1,0,0,0,1], n = 2
# 输出: False
#
#
# 注意:
#
#
# 数组内已种好的花不会违反种植规则。
# 输入的数组长度范围为 [1, 20000]。
# n 是非负整数，且不会超过输入数组的大小。
#
#
#
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if not flowerbed:
            return
        in_space = flowerbed[0] == 0
        space_len = 1 if in_space else 0   # 处理开头为空地的情况
        ans = 0
        for i in flowerbed:
            if in_space:
                if i == 0:
                    space_len += 1
                else:
                    ans += (space_len-1) // 2
                    space_len = 0
                    in_space = False
            else:
                if i == 0:
                    in_space = True
                    space_len += 1
        if space_len:  # 处理末尾为空地的情况
            ans += space_len // 2
        return ans >= n

if __name__ == "__main__":
    s = Solution().canPlaceFlowers(flowerbed = [0, 0, 0, 0, 1,0,0,0,1,0,0], n = 2)
    print(s)

