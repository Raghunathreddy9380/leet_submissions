class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        b = 0
        for i in range(len(s)):
            a = s[i]
            for j in range(1 + i, len(s)):
                if s[i] != s[j] and s[j] not in a:
                    a += s[j]
                elif s[i] == s[j] or s[j] in a:
                    break
            temp = len(a)
            if temp > b:
                b = temp
        return b   