class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for x in range(n):
            nums1.pop()
        start = 0
        end = 0
        while start < m and end < n:
            if nums1[start] < nums2[end]:
                start += 1
            else:
                print(start)
                nums1.insert(start,nums2[end])
                start += 1
                m += 1
                end += 1

        while end < n:
            nums1.append(nums2[end])
            end += 1

            