class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9+7
        freq = [0] * 26
    
        # Populate initial frequencies from string s
        for char in s:
            freq[ord(char) - ord('a')] += 1
        
        # Apply transformations
        for _ in range(t):
            new_freq = [0] * 26
            for i in range(26):
                if i == 25:  # 'z' case
                    new_freq[0] = (new_freq[0] + freq[i]) % MOD  # 'a'
                    new_freq[1] = (new_freq[1] + freq[i]) % MOD  # 'b'
                else:
                    new_freq[i + 1] = (new_freq[i + 1] + freq[i]) % MOD  # next character in alphabet
            freq = new_freq  # update frequency array
        
        # Calculate the final length of the string
        result_length = sum(freq) % MOD
        return result_length