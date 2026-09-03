class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        found = False
        esmallest = 10e5 
        osmallest = 10e5 - 1
    
        for i in range(len(nums1)):
            if nums1[i] % 2 == 0:
                esmallest = min(esmallest, nums1[i])
            else:
                osmallest = min(osmallest, nums1[i])
                found = True
        
        if found == False:
            return True
        else:
            if esmallest > osmallest:
                return True
            else:
                return False 