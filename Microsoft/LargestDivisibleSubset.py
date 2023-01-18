# Largest Divisible Subset - https://leetcode.com/problems/largest-divisible-subset
#Youtube Video - https://www.youtube.com/watch?v=IFfYfonAFGc&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=43

def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        dp = [1] * n
        hash = [i for i in range(n)]
        res = 1
        lastInd = 0
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    hash[i] = j
            if dp[i] > res:
                lastInd = i
                res = dp[i]
        ans = []
        print(hash, lastInd, dp, res)
        while lastInd != hash[lastInd]:
            ans.append(nums[lastInd])
            lastInd = hash[lastInd]
        ans.append(nums[lastInd])
        return ans

#Hash is used to store the previous index
#dp is 