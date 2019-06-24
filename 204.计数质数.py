#
# @lc app=leetcode.cn id=204 lang=python
#
# [204] 计数质数
#
# https://leetcode-cn.com/problems/count-primes/description/
#
# algorithms
# Easy (27.42%)
# Likes:    157
# Dislikes: 0
# Total Accepted:    19.6K
# Total Submissions: 69K
# Testcase Example:  '10'
#
# 统计所有小于非负整数 n 的质数的数量。
#
# 示例:
#
# 输入: 10
# 输出: 4
# 解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
#
#
#
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n < 2:
            return 0

        is_primes = [1 for i in range(n)]
        is_primes[0] = is_primes[1] = 0
        for i in range(2, n//2+1):
            if is_primes[i]:
                for j in range(i*i, n, i):
                    is_primes[j] = 0
        return sum(is_primes)

        # # 抄的高分答案, 很快, 应该是由于数组的多段赋值
        # if n < 3:       # 注意审题边界条件,是小于n,不包括n
        #     return 0    # 注意 数组越界的情况

        # primes = [1] * n
        # primes[0] = primes[1] = 0
        # for i in range(2, int(n**0.5)+1):    # 在选择除数时候的一个小技巧.大于一半的数是不可能做除数的
        #     if primes[i]:
        #         primes[i * i: n: i] = [0] * ((n - 1) // i - i + 1)  # 用埃氏筛法, 将每一个不是素数的数筛选掉.大大减少除法的数量.
        # return sum(primes)

if __name__ == "__main__":
    s = Solution().countPrimes(12)
    print(s)


