class Solution:
    def binaryGap(self, n: int) -> int:
        bstr=bin(n)[2:len(bin(n))]
        dist = 0
        maxDist = 0
        count = False;
        for i in range(len(bstr)-1, 0, -1):
            if count:
                if bstr[i] == '0':
                    dist = dist + 1
                else:
                    dist = 1
            else:
                if bstr[i] == '1':
                    count = True
                    dist = dist + 1
            if bstr[i] == '1' and bstr[i-1] =='1':
                dist = 1
                if dist > maxDist:
                    maxDist = dist
        
            if dist > maxDist:
                    maxDist = dist
        return maxDist