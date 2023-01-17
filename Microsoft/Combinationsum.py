# Combination Sum: https://leetcode.com/problems/combination-sum-iii/submissions/879618382/

class Solution:
    def getSum(self, n, k, ind, res, curr):
        if k == 0:
            if n == 0:
                res.append(curr)
            return
        if ind <= 0:
            return
        self.getSum(n, k, ind - 1, res, curr)
        self.getSum(n - ind, k - 1, ind - 1, res, curr + [ind])
        

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.getSum(n, k, 9, res, [])
        return res