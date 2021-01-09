from collections import deque
class RecentCounter:
    def __init__(self):
        self.requests = deque()
        
    def ping(self, t: int) -> int:
        self.requests.append(t)
        start_index = (t-3000) if (t-3000) > 0 else 1
        while(self.requests[0] < start_index):
            self.requests.popleft()
        return len(self.requests)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)