# 581. Shortest Unsorted Continuous Subarray:
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        ptr1 = 0
        ptr2 = len(nums) - 1
        n = len(nums)
        while ptr1 < n - 1:
            if nums[ptr1] <= nums[ptr1 + 1]:
                ptr1 += 1
            else:
                break
        while ptr2 > 0:
            if nums[ptr2] >= nums[ptr2 - 1]:
                ptr2 -= 1
            else:
                break
        print(ptr1, ptr2)
        if ptr1 < ptr2:
            ind1 = bisect.bisect_right(nums[:ptr1 + 1], nums[ptr1 + 1])
            ind2 = bisect.bisect_left(nums[ptr2:], nums[ptr2 - 1])
            return (ind2 + ptr2 - ind1)
        return 0


# Appr2
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        mini = 1000000000
        maxi = -1000000000
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                mini = min(mini, nums[i])
        for i in range(n - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                maxi = max(maxi, nums[i])
        if mini == 1000000000 or maxi == -1000000000:
            return 0

        for i in range(n):
            if nums[i] > mini:
                ind1 = i
                break
        for i in range(n - 1, -1, -1):
            if nums[i] < maxi:
                ind2 = i
                break
        return abs(ind2 - ind1 + 1)


# O(N) solution
