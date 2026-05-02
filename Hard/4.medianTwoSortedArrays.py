class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        m, n = len(nums1), len(nums2)
        left, right = 0, m
        
        while left <= right:
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i
            
            nums1LeftMax = float('-inf') if i == 0 else nums1[i-1]
            nums1RightMin = float('inf') if i == m else nums1[i]
            nums2LeftMax = float('-inf') if j == 0 else nums2[j-1]
            nums2RightMin = float('inf') if j == n else nums2[j]
            
            if nums1LeftMax <= nums2RightMin and nums2LeftMax <= nums1RightMin:
                if (m + n) % 2:
                    return max(nums1LeftMax, nums2LeftMax)
                return (max(nums1LeftMax, nums2LeftMax) + min(nums1RightMin, nums2RightMin)) / 2
            elif nums1LeftMax > nums2RightMin:
                right = i - 1
            else:
                left = i + 1
        
        return 0.0
                  