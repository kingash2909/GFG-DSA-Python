
class TwoStacks:
    def __init__(self,n=10000):
        self.size = n
        self.arr = [0] * n
        self.top1 = -1  # Initialize top pointer for stack 1
        self.top2 = self.size  # Initialize top pointer for stack 2

    # Function to push an integer into stack 1
    def push1(self, x):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.arr[self.top1] = x

    # Function to push an integer into stack 2
    def push2(self, x):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.arr[self.top2] = x

    # Function to remove an element from top of stack 1
    def pop1(self):
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.top1 -= 1
            return x
        return -1

    # Function to remove an element from top of stack 2
    def pop2(self):
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.top2 += 1
            return x
        return -1
