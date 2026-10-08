class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def freq_count(s):
            freq = {}
            for c in s:
                freq[c] = freq.get(c, 0) + 1
            return freq
        return freq_count(s) == freq_count(t)