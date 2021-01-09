class Solution:
    def romanToInt(self, s: str) -> int:
        r = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000,
            'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        num = 0
        i = 1
        s += " "
        while i < len(s):
            if ((s[i] == 'V' or s[i] == 'X') and s[i-1] == 'I') or ((s[i] == 'L' or s[i] == 'C') and s[i-1] == 'X') or ((s[i] == 'D' or s[i] == 'M') and s[i-1] == 'C'):
                num = num + r[s[i-1]+s[i]]
                i = i + 2
                continue
            else:
                num = num + r[s[i-1]]
                i = i + 1
        return num