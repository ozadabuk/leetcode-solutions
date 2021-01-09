class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)-1
        for i in range(0, (n+1)//2):
            tmp = s[n-i]
            s[n-i] = s[i]
            s[i] = tmp