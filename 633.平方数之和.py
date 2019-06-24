#
# @lc app=leetcode.cn id=633 lang=python
#
# [633] 平方数之和
#
# https://leetcode-cn.com/problems/sum-of-square-numbers/description/
#
# algorithms
# Easy (29.91%)
# Likes:    58
# Dislikes: 0
# Total Accepted:    6.1K
# Total Submissions: 19.7K
# Testcase Example:  '5'
#
# 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a^2 + b^2 = c。
#
# 示例1:
#
#
# 输入: 5
# 输出: True
# 解释: 1 * 1 + 2 * 2 = 5
#
#
#
#
# 示例2:
#
#
# 输入: 3
# 输出: False
#
#
#
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        # # 暴力二分查找, 超时
        # import math
        # def func(base):
        #     f = lambda x: x**2 + base
        #     i = -1
        #     j = int(math.sqrt(c)) + 1
        #     while i < j-1:
        #         # print(i, j)
        #         mid = (i+j)//2
        #         if f(mid) > c:
        #             j = mid
        #         elif f(mid) < c:
        #             i = mid
        #         else:
        #             return True
        #     return False

        # for i in range(int(math.sqrt(c))+1):
        #     if func(i**2):
        #         return True
        # return False
        # long int a = sqrt(c);
        # if(a == sqrt(c)) return 1;
        # long int b = 1;
        # long int d = a;
        # while((b + d > a) && (d - b < a))
        # {
        #     if(c == b*b + d*d) return 1;
        #     else if(c > b*b + d*d) b++;
        #     else d--;
        # }
        # return 0;

        import math
        a = math.sqrt(c)
        if a == int(a):
            return True
        a = int(a)
        b = 1
        d = a
        while (b + d > a) and (d - b < a):
            if c == b ** 2 + d ** 2:
                return True
            elif c > b ** 2 + d ** 2:
                b += 1
            else:
                d -= 1
        return False

        # # 最快的答案, 抄的
        # if not c:
        #     return True
        # k = int(math.sqrt(c))
        # l = int(math.sqrt(c/2))
        # for i in range(k, l-1,-1):
        #     m = math.sqrt(c - i*i)
        #     if int(m) == m:
        #         return True
        # return False

if __name__ == "__main__":
    s = Solution().judgeSquareSum(4)
    print(s)
    s = Solution().judgeSquareSum(0)
    print(s)
    s = Solution().judgeSquareSum(5)
    print(s)
    s = Solution().judgeSquareSum(6)
    print(s)

