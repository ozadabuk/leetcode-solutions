class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        s += " "
        score = 0
        count = 1
        groups = []
        for i in range(1, len(s)):
            if s[i] is s[i-1]:
                count = count + 1
            else:
                groups.append(count)
                count = 1
        for i in range(0, len(groups)-1):
            score = score + min(groups[i], groups[i+1])
        return score