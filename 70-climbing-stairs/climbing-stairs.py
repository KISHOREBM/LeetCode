def find(n, memo={}):
    if n <= 1:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = find(n - 1, memo) + find(n - 2, memo)
    return memo[n]

class Solution(object):
    def climbStairs(self, n):
        return find(n)
