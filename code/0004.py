class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findk(l1, l2, k):
            if len(l1) == 0:
                return l2[k]
            if len(l2) == 0:
                return l1[k]
            idx1, idx2 = len(l1) // 2, len(l2) // 2
            val1, val2 = l1[idx1], l2[idx2]
            if idx1 + idx2 < k:
                if val1 > val2: # remove l2 first half
                    return findk(l1, l2[idx2+1:], k-idx2-1)
                else: # remove l1 first half
                    return findk(l1[idx1+1:], l2, k-idx1-1)
            else:
                if val1 > val2:  # remove l1 back half
                    return findk(l1[:idx1], l2, k)
                else:  # remove l2 back half
                    return findk(l1, l2[:idx2], k)
        len1 = len(nums1)
        len2 = len(nums2)
        if (len1 + len2) % 2 == 0: # ex [0, 1, 2, 3] -> [1, 2]
            return (findk(nums1, nums2, (len1+len2)//2-1) + findk(nums1, nums2, (len1+len2)//2)) / 2
        else: # ex [0, 1, 2] -> [1]
            return findk(nums1, nums2, (len1+len2)//2)
      