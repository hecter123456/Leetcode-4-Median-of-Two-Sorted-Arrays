import unittest
import heapq

class unitest(unittest.TestCase):
    def testOneOddList(self):
        nums1 = [1,2,3,4]
        nums2 = []
        Ans = 2.5
        self.assertEqual(Solution().findMedianSortedArrays(nums1,nums2),Ans);
    def testOneEvenList(self):
        nums1 = [1,2,3]
        nums2 = []
        Ans = 2
        self.assertEqual(Solution().findMedianSortedArrays(nums1,nums2),Ans);
    def testNumberOddList(self):
        nums1 = [1,3]
        nums2 = [2]
        Ans = 2
        self.assertEqual(Solution().findMedianSortedArrays(nums1,nums2),Ans);
    def testNumberEvenList(self):
        nums1 = [1,4]
        nums2 = [2,3]
        Ans = 2.5
        self.assertEqual(Solution().findMedianSortedArrays(nums1,nums2),Ans);

class Solution():
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1),len(nums2)
        # let n > m
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        imin, imax, halfLen = 0, m, (n + m + 1) / 2
        # i+j == m-i+n-j+1
        while imin <= imax:
            i = int((imin + imax)/2)
            j = int(halfLen - i)
            # j == 0 or i == m or B[j-1] <= A[i]
            if i < m and nums2[j-1] > nums1[i]:
                imin = i + 1
            # i == 0 or j = n or A[i-1] <= B[j]
            elif i > 0 and nums1[i-1] > nums2[j]:
                imax = i - 1
            else:
                if i == 0:
                    max_of_left = nums2[j-1]
                elif j == 0:
                    max_of_left = nums1[i-1]
                else:
                    max_of_left = max(nums1[i-1],nums2[j-1])
                # m+n is odd
                if (m + n) % 2 == 1:
                    return max_of_left
                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i],nums2[j])
                return (max_of_left + min_of_right) / 2.0
if __name__ == '__main__':
    unittest.main()
