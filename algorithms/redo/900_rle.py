class RLEIterator:
    def __init__(self, A: List[int]):
        self.quantity = 0
        self.index = 0
        self.array = A

    def next(self, n: int) -> int:
        while self.index < len(self.array):
            if self.quantity + n > self.array[self.index]:
                n -= self.array[self.index] - self.quantity
                self.quantity = 0
                self.index += 2
            else:
                self.quantity += 2
                return self.array[self.index + 1]


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)
