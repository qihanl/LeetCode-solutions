# Original problem: https://leetcode.com/problems/median-of-two-sorted-arrays/solution/

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]:m
        :type nums2: List[int]:n
        :rtype: float
        """
        if len(nums1) == 0:
            return (nums2[len(nums2)/2] + nums2[(len(nums2)-1)/2]) / 2.0
        elif len(nums2) == 0:
            return (nums1[len(nums1)/2] + nums1[(len(nums1)-1)/2]) / 2.0
        
        merged = []
        m = 0
        n = 0
        if(nums1[m] < nums2[n]):
            merged.append(nums1[m])
            m += 1
        else:
            merged.append(nums2[n])
            n += 1
        while m!=len(nums1) and n!=len(nums2):
            if(nums1[m] < nums2[n]):
                merged.append(nums1[m])
                m += 1
            else:
                merged.append(nums2[n])
                n += 1
        if m!=len(nums1):
            for i in range(m, len(nums1)):
                merged.append(nums1[i])
        elif n!=len(nums2):
            for i in range(n, len(nums2)):
                merged.append(nums2[i])
                
        return (merged[len(merged)/2] + merged[(len(merged)-1)/2]) / 2.0
