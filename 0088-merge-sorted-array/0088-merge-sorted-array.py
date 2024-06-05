class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        first = 0
        second = 0
        for i in range(n):
            nums1.pop()
        while first < len(nums1) and second < len(nums2):
            print(nums1)
            if nums1[first] <= nums2[second]:
                first += 1
            else:
                nums1.insert(first,nums2[second])
                first += 1
                second += 1
        # first += 1
        while second < n:
            nums1.insert(first,nums2[second])
            first += 1
            second += 1