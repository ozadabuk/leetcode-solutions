class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        m = 0
        for item in nums:
            if item in d:
                d[item] = d[item] + 1
            else:
                d[item] = 1
                
        for k, v in d.items():
            if v == 1:
                m = k
                break
        return m