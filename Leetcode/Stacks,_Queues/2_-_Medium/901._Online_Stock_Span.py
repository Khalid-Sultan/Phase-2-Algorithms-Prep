class StockSpanner:

    def __init__(self):
        self.stack = deque() 

    def next(self, price: int) -> int:
        ct = 1
        if not self.stack:
            self.stack.append((price, 1))
        else:
            if self.stack[-1][0]>price:
                self.stack.append((price,1))
            else:
                while self.stack and self.stack[-1][0]<=price:
                    ct+=self.stack.pop()[1]
                self.stack.append((price,ct))
        return ct

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
