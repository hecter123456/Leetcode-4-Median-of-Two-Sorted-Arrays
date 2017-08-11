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
        a = list(heapq.merge(nums1,nums2))
        mid = int(len(a)/2)
        if len(a)%2:
            return a[mid]
        else:
            return (float(a[mid-1]) + float(a[mid]))/2

if __name__ == '__main__':
    unittest.main()
