class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        if len(intervals) < 2:
            return [-1]
        rii = []
        items = sorted(enumerate(intervals), key=lambda x: x[1][0])
        for k in items:
            res = self.binarySearch(k, items)
            rii.append(res)
        z = zip(items, rii)
        res = [[0] * i for i in range(len(items))]
        for i, r in z:
            res[i[0]] = r
        return res
    
    def binarySearch(self, k, items):
        mid = len(items) // 2
        _max = len(items)
        _min = 0
        last_start_j = 0
        last_start_j_index = 0
        while _min < _max + 1:
            if k[1][1] > items[mid][1][0]:
                last_start_j = items[mid][1][0]
                last_start_j_index = mid
                _min = mid
                mid = (_max + _min) // 2
                if len(items[mid:_max]) == 1:
                    if k[1][1] < items[mid][1][0]:
                        break
                    elif k[1][1] > items[mid][1][0]:
                        mid = -1
                        break
            elif k[1][1] < items[mid][1][0]:
                last_start_j = items[mid][1][0]
                last_start_j_index = mid
                if mid - 1 > -1:
                    if k[1][1] > items[mid - 1][1][0]:
                        break
                    
                _max = mid
                mid = (_max + _min) // 2
                if len(items[_min:_max]) == 0 and last_start_j > k[1][1]:
                    mid = last_start_j_index
                    break
                elif len(items[_min:_max]) == 0 and last_start_j < k[1][1]:
                    mid = -1
                    break
            else:
                break
        if mid == -1:
            return mid
        else:
            return items[mid][0]

                    