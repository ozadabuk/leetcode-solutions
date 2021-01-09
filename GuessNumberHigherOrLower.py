# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        if n == 1:
            return 1
        min_ = 0
        mid = n//2
        max_ = n
        max_ = max_ + 1
        m = 2
        while m != 0:
            m = guess(mid)
            if m == 1:
                min_ = mid
                mid = (max_ + mid)//2
            elif m == -1:
                max_ = mid
                mid = (max_ + min_)//2
            else:
                break
        return mid