from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        cd = {}
        sq = deque(s)
        while sq:
            done = False
            i = 0
            while (done == False) and (i < len(sq)):
                ch=sq[i]
                if ch in cd: 
                    done = True
                    if len(cd) > maxlen:
                        maxlen = len(cd)
                    sq.popleft()
                    cd = {}
                else:
                    cd[ch] = ch    
                i = i + 1
                
        return maxlen