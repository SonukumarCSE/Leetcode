class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        print(numset)
        for n in numset:
            if n-1 not in numset:
                length = 0
                while n + length in numset:
                    length += 1
                longest = max(longest,length)
        return longest