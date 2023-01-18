#rotation function: https://leetcode.com/problems/rotate-function

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        s = sum(nums)
        ans = val = sum([i * j for (i, j) in enumerate(nums)])
        for i in range(1, n):
            val = val + s - n * nums[-i]
            print(val)
            ans = max(ans, val)
        return ans

#f(0) = 0 * ar[0] + 1 * ar[1] + ..... (n - 1) * ar[n - 1]
#f(1) = 0 * ar[n - 1] + 1 * ar[0] + ..... (n - 1) * ar[n - 2]
#.
#.
#.
#f(n - 1) = ....
#f[1] - f[0] = ar[0] + ar[1] ... ar[n - 2] - (n - 1) * ar[n - 1]
#f[1] - f[0] = ar[0] + ar[1] + .. ar[n - 1] - n * ar[n - 1]
#f[1] - f[0] = s - n * ar[n - 1]
#f[1] = f[0] + s - n * ar[n - 1]