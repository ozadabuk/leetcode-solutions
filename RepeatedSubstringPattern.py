class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if not s:
            return False
        sb = ""
        n = len(s)
        i = 0
        while i < n//2:
            sb = sb + s[i]
            i = i + 1
            t = ceil(n/i)
            if sb * t == s:
                return True
        return False