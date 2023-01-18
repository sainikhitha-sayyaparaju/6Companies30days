# 2426. Number of Pairs Satisfying Inequality: https://leetcode.com/problems/number-of-pairs-satisfying-inequality/


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1)
        nums = [nums1[0] - nums2[0] - diff]
        res = 0
        for i in range(1, n):
            ind = bisect.bisect_right(nums, nums1[i] - nums2[i])
            if ind == 0 and nums[0] != nums1[i] - nums2[i]:
                pass
            elif ind == 0:
                res += 1
            elif ind == n:
                res += n
            elif ind < i and nums[ind] == nums1[i] - nums2[i]:
                res += ind + 1
            else:
                res += ind
            nums.insert(bisect.bisect_left(
                nums, nums1[i] - nums2[i] - diff), nums1[i] - nums2[i] - diff)
            # print(nums, res, ind, nums1[i] - nums2[i])
        return res

# nums1[i] - nums1[j] - diff <= nums2[i] - nums2[j]
# Here I took a list nums and appended
# Every time I search for nums2[i] - nums2[j] in the nums and count the res
# and now using bin search I am appending nums1[i] - nums1[j] - diff into the nums
