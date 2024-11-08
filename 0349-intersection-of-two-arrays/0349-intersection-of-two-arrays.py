from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        map = {}
        
        # Fill the map with counts of elements in nums1
        for i in nums1:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1
        
        # Check elements in nums2 for intersection
        for j in nums2:
            if j in map and map[j] > 0:
                res.append(j)
                map[j] = 0  # Set count to 0 to avoid duplicates in the result
                
        return res
