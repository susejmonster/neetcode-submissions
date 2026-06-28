class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 0
        self.stack.append(price)
        for s in range(len(self.stack)-1,-1,-1):
            if self.stack[s] <= price:
                span+=1
            else:
                break
        return span



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)