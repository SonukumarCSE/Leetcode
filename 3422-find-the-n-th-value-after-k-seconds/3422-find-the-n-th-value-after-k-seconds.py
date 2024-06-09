class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        a = [1] * n
        
        for _ in range(k):
            cumulative_sum = 0
            for i in range(n):
                cumulative_sum = (cumulative_sum + a[i]) % MOD
                a[i] = cumulative_sum
        
        return a[-1]