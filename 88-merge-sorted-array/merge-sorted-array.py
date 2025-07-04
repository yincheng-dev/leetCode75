class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # set up 3 pointers p1, p2, p
        # p1 : last valid element in nums1
        p1 = m - 1
        # p2 : last element in nums2
        p2 = n-1
        # p  : last position in nums1
        p = m + n -1

        # Step 1 : Merge the nums2 to nums1 from the end
        # while current p1 is bigger, put it in the end 
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1 # move pointer left in nums1
            # while current p2 is bigger, put it in the end 
            else:
                nums1[p] = nums2[p2]
                p2 -= 1 # move pointer left in nums2
            p -= 1  # move left so we are placing next

        # Step 2 : If anything left in nums 2, copy it to nums1
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p  -= 1       


    
        