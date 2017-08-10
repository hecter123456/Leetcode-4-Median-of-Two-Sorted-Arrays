import unittest

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

class Solution():
    def findMedianSortedArrays(self, nums1, nums2):
        if not nums1:
            tmp = nums2
        if not nums2:
            tmp = nums1
        mid = int(len(tmp)/2)
        if len(tmp) % 2:
            Ans = tmp[mid]
        else:
            Ans = (tmp[mid-1]+tmp[mid])/2
        return Ans

if __name__ == '__main__':
    unittest.main()
