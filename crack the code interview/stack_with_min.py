import sys


class MinStack:

    def __init__(self, stacksize):
        self.array = []
        self.stacksize = stacksize
        self.minvals = []

    def Peek(self):
        return self.array[-1]

    def isEmpty(self):
        return len(self.array) == 0 

    def isFull(self):
        return len(self.array) == self.stacksize

    def Push(self,item):
        if self.isFull():
            raise Exception('Stack is Full.')
        if self.isEmpty():
            self.minvals.append(item)
        else:
            self.minvals.append(min(item,self.minvals[-1]))

        self.array.append(item)


    def Pop(self):
        if self.isEmpty():
            raise Exception('Stack is empty.')
        self.minvals.pop()
        return self.array.pop()

    def print_all(self):
        return self.array


    def print_min(self):
        return self.minvals

    def Min(self):
        return self.minvals[-1]




def StackMin():
    newstack = MinStack(10)
    newstack.Push(5)
    newstack.Push(6)
    newstack.Push(9)
    newstack.Push(7)
    newstack.Push(14)
    newstack.Push(3)
    print '---show all data---'
    print newstack.print_all()
    print '---show all min---'
    print newstack.print_min()
    print newstack.Min()
    newstack.Pop()
    print '---show all data---'
    print newstack.print_all()
    print '---show all min---'
    print newstack.print_min()
    print newstack.Min()
    newstack.Push(1)
    newstack.Push(4)
    newstack.Push(44)
    newstack.Push(2)
    print '---show all data---'
    print newstack.print_all()
    print '---show all min---'
    print newstack.print_min()
    print newstack.Min()

StackMin()
